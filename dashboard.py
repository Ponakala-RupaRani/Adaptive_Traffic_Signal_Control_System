import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

# =====================================================
# SMART TRAFFIC AI - FOUR WAY ADAPTIVE SIGNAL PROTOTYPE
# =====================================================

VIDEO_FILE = "traffic.mp4"

# -----------------------------------------------------
# DEMO COUNTS
# Change these numbers to demonstrate different traffic
# conditions at each direction.
# -----------------------------------------------------

traffic = {
    "NORTH": 12,
    "EAST": 20,
    "SOUTH": 5,
    "WEST": 8
}

# -----------------------------------------------------
# Green-time calculation
# -----------------------------------------------------

def get_density(count):
    if count <= 5:
        return "LOW"
    elif count <= 10:
        return "MEDIUM"
    else:
        return "HIGH"


def get_green_time(count):
    if count <= 5:
        return 20
    elif count <= 10:
        return 30
    elif count <= 15:
        return 40
    else:
        return 60


for direction in traffic:
    traffic[direction] = int(traffic[direction])


# -----------------------------------------------------
# Main Window
# -----------------------------------------------------

root = tk.Tk()
root.title("Smart Traffic AI - Adaptive Traffic Signal Control")
root.geometry("1250x780")
root.configure(bg="#111827")


# -----------------------------------------------------
# Title
# -----------------------------------------------------

title = tk.Label(
    root,
    text="SMART TRAFFIC AI",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="#111827"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Adaptive Four-Way Traffic Signal Control",
    font=("Arial", 16),
    fg="#9ca3af",
    bg="#111827"
)
subtitle.pack()


# -----------------------------------------------------
# Video
# -----------------------------------------------------

video_frame = tk.Frame(
    root,
    bg="black",
    width=650,
    height=450
)
video_frame.place(x=30, y=100)

video_label = tk.Label(
    video_frame,
    bg="black"
)
video_label.pack()


video = cv2.VideoCapture(VIDEO_FILE)


def play_video():

    success, frame = video.read()

    if success:

        frame = cv2.resize(frame, (650, 450))

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(frame)

        photo = ImageTk.PhotoImage(image)

        video_label.configure(
            image=photo
        )

        video_label.image = photo

        root.after(30, play_video)

    else:

        video.set(
            cv2.CAP_PROP_POS_FRAMES,
            0
        )

        root.after(30, play_video)


# -----------------------------------------------------
# Direction Panel
# -----------------------------------------------------

panel = tk.Frame(
    root,
    bg="#1f2937"
)

panel.place(
    x=710,
    y=100,
    width=500,
    height=450
)


heading = tk.Label(
    panel,
    text="LIVE TRAFFIC ANALYSIS",
    font=("Arial", 21, "bold"),
    fg="white",
    bg="#1f2937"
)
heading.pack(pady=15)


direction_labels = {}


for direction in ["NORTH", "EAST", "SOUTH", "WEST"]:

    count = traffic[direction]

    density = get_density(count)

    green = get_green_time(count)

    row = tk.Frame(
        panel,
        bg="#1f2937"
    )

    row.pack(
        fill="x",
        padx=20,
        pady=8
    )

    direction_label = tk.Label(
        row,
        text=direction,
        font=("Arial", 17, "bold"),
        fg="white",
        bg="#1f2937",
        width=10,
        anchor="w"
    )

    direction_label.pack(side="left")

    count_label = tk.Label(
        row,
        text=f"{count} vehicles",
        font=("Arial", 16),
        fg="white",
        bg="#1f2937",
        width=14
    )

    count_label.pack(side="left")

    density_label = tk.Label(
        row,
        text=density,
        font=("Arial", 15, "bold"),
        fg="yellow",
        bg="#1f2937",
        width=10
    )

    density_label.pack(side="left")

    green_label = tk.Label(
        row,
        text=f"{green}s",
        font=("Arial", 16, "bold"),
        fg="lime",
        bg="#1f2937",
        width=8
    )

    green_label.pack(side="left")

    direction_labels[direction] = {
        "count": count_label,
        "density": density_label,
        "green": green_label
    }


# -----------------------------------------------------
# Find Highest Traffic Direction
# -----------------------------------------------------

highest_direction = max(
    traffic,
    key=traffic.get
)

highest_count = traffic[highest_direction]

highest_green = get_green_time(
    highest_count
)


priority_label = tk.Label(
    panel,
    text=(
        f"PRIORITY: {highest_direction}\n"
        f"Highest Traffic: {highest_count} vehicles\n"
        f"Green Time: {highest_green} seconds"
    ),
    font=("Arial", 18, "bold"),
    fg="cyan",
    bg="#1f2937"
)

priority_label.pack(pady=15)


# -----------------------------------------------------
# Signal Display
# -----------------------------------------------------

signal_frame = tk.Frame(
    root,
    bg="#030712"
)

signal_frame.place(
    x=30,
    y=580,
    width=650,
    height=150
)


signal_title = tk.Label(
    signal_frame,
    text="CURRENT SIGNAL",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#030712"
)

signal_title.pack(pady=8)


signal_label = tk.Label(
    signal_frame,
    text=f"🟢 {highest_direction} GREEN",
    font=("Arial", 25, "bold"),
    fg="lime",
    bg="#030712"
)

signal_label.pack()


timer_label = tk.Label(
    signal_frame,
    text=f"Green Time: {highest_green} seconds",
    font=("Arial", 16),
    fg="white",
    bg="#030712"
)

timer_label.pack()


# -----------------------------------------------------
# Green Corridor
# -----------------------------------------------------

def green_corridor():

    signal_label.config(
        text="🚨 GREEN CORRIDOR ACTIVE",
        fg="red"
    )

    timer_label.config(
        text="Emergency Route: PRIORITY GREEN"
    )

    priority_label.config(
        text=(
            "🚨 EMERGENCY VEHICLE DETECTED\n"
            "Green Corridor Activated\n"
            "Priority Route: NORTH → EAST"
        ),
        fg="red"
    )


corridor_button = tk.Button(
    root,
    text="🚨 ACTIVATE GREEN CORRIDOR",
    font=("Arial", 17, "bold"),
    bg="#dc2626",
    fg="white",
    padx=15,
    pady=10,
    command=green_corridor
)

corridor_button.place(
    x=710,
    y=590,
    width=500,
    height=60
)


# -----------------------------------------------------
# Explanation
# -----------------------------------------------------

info = tk.Label(
    root,
    text=(
        "AI Decision: Higher vehicle density → Longer Green Time"
    ),
    font=("Arial", 15),
    fg="#d1d5db",
    bg="#111827"
)

info.place(
    x=710,
    y=670
)


# -----------------------------------------------------
# Start Video
# -----------------------------------------------------

play_video()

root.mainloop()