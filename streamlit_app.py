import streamlit as st
import cv2
import tempfile
import os
from ultralytics import YOLO

st.set_page_config(
    page_title="Smart Traffic AI",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Smart Traffic AI")
st.subheader("AI-Based Four-Way Traffic Management System")

uploaded_file = st.file_uploader(
    "Upload traffic.mp4",
    type=["mp4"]
)

if uploaded_file is not None:

    if st.button("🚦 Start YOLO Traffic Detection"):

        # Save uploaded video
        input_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        ).name

        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info("Loading YOLO model...")

        model = YOLO("yolov8n.pt")

        cap = cv2.VideoCapture(input_path)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 24

        output_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        ).name

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        writer = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (width, height)
        )

        progress = st.progress(0)

        total_frames = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        frame_no = 0

        # Vehicle classes
        vehicle_classes = [2, 3, 5, 7]

        # Stable maximum counts
        north_max = 0
        east_max = 0
        south_max = 0
        west_max = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            results = model.predict(
                frame,
                conf=0.15,
                imgsz=640,
                classes=vehicle_classes,
                verbose=False
            )

            north = 0
            east = 0
            south = 0
            west = 0

            for result in results:

                if result.boxes is None:
                    continue

                for box in result.boxes:

                    class_id = int(box.cls[0])

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    cx = (x1 + x2) // 2
                    cy = y2

                    # -----------------------------
                    # FOUR WAY DETECTION
                    # -----------------------------

                    if 100 < cx < 450 and 20 < cy < 330:

                        north += 1
                        label = "NORTH"

                    elif 300 < cx < 608 and 250 < cy < 650:

                        east += 1
                        label = "EAST"

                    elif 100 < cx < 520 and 650 < cy < 1080:

                        south += 1
                        label = "SOUTH"

                    elif 0 < cx < 300 and 250 < cy < 700:

                        west += 1
                        label = "WEST"

                    else:

                        label = "JUNCTION"

                    # Draw bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    cv2.putText(
                        frame,
                        label,
                        (x1, max(20, y1 - 8)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2
                    )

                    cv2.circle(
                        frame,
                        (cx, cy),
                        4,
                        (0, 0, 255),
                        -1
                    )

            # Keep highest recent count
            north_max = max(north_max, north)
            east_max = max(east_max, east)
            south_max = max(south_max, south)
            west_max = max(west_max, west)

            # -----------------------------
            # DRAW ROI BOXES
            # -----------------------------

            cv2.rectangle(
                frame,
                (100, 20),
                (450, 330),
                (255, 0, 0),
                2
            )

            cv2.rectangle(
                frame,
                (300, 250),
                (608, 650),
                (0, 255, 255),
                2
            )

            cv2.rectangle(
                frame,
                (100, 650),
                (520, 1070),
                (0, 255, 0),
                2
            )

            cv2.rectangle(
                frame,
                (0, 250),
                (300, 700),
                (255, 0, 255),
                2
            )

            # -----------------------------
            # INFO PANEL
            # -----------------------------

            cv2.rectangle(
                frame,
                (0, 0),
                (width, 180),
                (0, 0, 0),
                -1
            )

            cv2.putText(
                frame,
                f"NORTH : {north_max}",
                (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"EAST  : {east_max}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"SOUTH : {south_max}",
                (10, 105),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"WEST  : {west_max}",
                (10, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 255, 255),
                2
            )

            writer.write(frame)

            frame_no += 1

            if total_frames > 0:

                progress.progress(
                    min(frame_no / total_frames, 1.0)
                )

        cap.release()
        writer.release()

        progress.progress(1.0)

        # -----------------------------
        # FINAL TRAFFIC RESULTS
        # -----------------------------

        traffic = {
            "NORTH": north_max,
            "EAST": east_max,
            "SOUTH": south_max,
            "WEST": west_max
        }

        def density(n):

            if n <= 2:
                return "LOW"

            elif n <= 4:
                return "MEDIUM"

            return "HIGH"

        def green_time(n):

            if n <= 2:
                return 20

            elif n <= 4:
                return 30

            return 45

        priority = max(
            traffic,
            key=traffic.get
        )

        st.success(
            "✅ YOLO Detection Completed!"
        )

        st.header("📊 Four-Way Traffic Analysis")

        c1, c2, c3, c4 = st.columns(4)

        for col, side in zip(
            [c1, c2, c3, c4],
            ["NORTH", "EAST", "SOUTH", "WEST"]
        ):

            with col:

                st.metric(
                    side,
                    f"{traffic[side]} vehicles"
                )

                st.write(
                    f"Density: **{density(traffic[side])}**"
                )

                st.write(
                    f"Green: **{green_time(traffic[side])} sec**"
                )

        st.success(
            f"🚦 PRIORITY: {priority} | "
            f"GREEN SIGNAL: {green_time(traffic[priority])} seconds"
        )

        st.header("🎥 YOLO Detected Video")

        # Read processed video
        with open(output_path, "rb") as video_file:

            video_bytes = video_file.read()

        st.video(video_bytes)

        st.caption(
            "YOLO vehicle detection + four-way traffic analysis"
        )
