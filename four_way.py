import cv2

# =========================================================
# SMART TRAFFIC AI - PRESENTATION DEMO
# =========================================================

VIDEO_PATH = "traffic.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("ERROR: traffic.mp4 not found")
    exit()

# =========================================================
# FIXED DEMO COUNTS
# =========================================================

counts = {
    "NORTH": 3,
    "EAST": 4,
    "SOUTH": 5,
    "WEST": 2
}

# =========================================================
# DENSITY
# =========================================================

def get_density(n):

    if n <= 2:
        return "LOW"

    elif n <= 4:
        return "MEDIUM"

    else:
        return "HIGH"


# =========================================================
# GREEN TIME
# =========================================================

def get_green(n):

    if n <= 2:
        return 20

    elif n <= 4:
        return 30

    else:
        return 45


# =========================================================
# PRIORITY
# =========================================================

priority = max(
    counts,
    key=counts.get
)

priority_count = counts[priority]
priority_green = get_green(priority_count)

# =========================================================
# MAIN LOOP
# =========================================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------------------------------
    # Original video = 608 x 1080
    # -----------------------------------------------------

    # =====================================================
    # TOP INFORMATION PANEL
    # =====================================================

    cv2.rectangle(
        frame,
        (0, 0),
        (608, 210),
        (0, 0, 0),
        -1
    )

    cv2.putText(
        frame,
        "SMART TRAFFIC AI",
        (150, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"NORTH : {counts['NORTH']} | "
        f"{get_density(counts['NORTH'])} | "
        f"GREEN {get_green(counts['NORTH'])}s",
        (15, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"EAST  : {counts['EAST']} | "
        f"{get_density(counts['EAST'])} | "
        f"GREEN {get_green(counts['EAST'])}s",
        (15, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"SOUTH : {counts['SOUTH']} | "
        f"{get_density(counts['SOUTH'])} | "
        f"GREEN {get_green(counts['SOUTH'])}s",
        (15, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"WEST  : {counts['WEST']} | "
        f"{get_density(counts['WEST'])} | "
        f"GREEN {get_green(counts['WEST'])}s",
        (15, 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 255),
        2
    )

    # =====================================================
    # FOUR SIDE ROAD BOXES
    # =====================================================

    # NORTH
    cv2.rectangle(
        frame,
        (100, 210),
        (450, 350),
        (255, 0, 0),
        3
    )

    cv2.putText(
        frame,
        "NORTH - 3 VEHICLES",
        (115, 240),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 0, 0),
        2
    )

    # EAST
    cv2.rectangle(
        frame,
        (350, 350),
        (608, 700),
        (0, 255, 255),
        3
    )

    cv2.putText(
        frame,
        "EAST - 4 VEHICLES",
        (355, 385),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.50,
        (0, 255, 255),
        2
    )

    # SOUTH
    cv2.rectangle(
        frame,
        (100, 700),
        (520, 1070),
        (0, 255, 0),
        3
    )

    cv2.putText(
        frame,
        "SOUTH - 5 VEHICLES",
        (115, 735),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.50,
        (0, 255, 0),
        2
    )

    # WEST
    cv2.rectangle(
        frame,
        (0, 350),
        (300, 700),
        (255, 0, 255),
        3
    )

    cv2.putText(
        frame,
        "WEST - 2 VEHICLES",
        (10, 385),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.50,
        (255, 0, 255),
        2
    )

    # =====================================================
    # SMART SIGNAL PANEL
    # =====================================================

    cv2.rectangle(
        frame,
        (110, 430),
        (495, 630),
        (0, 0, 0),
        -1
    )

    cv2.rectangle(
        frame,
        (110, 430),
        (495, 630),
        (0, 255, 0),
        3
    )

    cv2.putText(
        frame,
        "SMART SIGNAL",
        (200, 470),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"PRIORITY : {priority}",
        (175, 515),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"TRAFFIC  : {priority_count}",
        (175, 555),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"GREEN    : {priority_green} SEC",
        (165, 595),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (0, 255, 0),
        2
    )

    # =====================================================
    # DISPLAY
    # =====================================================

    display = cv2.resize(
        frame,
        (608, 900)
    )

    cv2.imshow(
        "SMART TRAFFIC AI - FINAL DEMO",
        display
    )

    # Q = quit
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Demo completed.")