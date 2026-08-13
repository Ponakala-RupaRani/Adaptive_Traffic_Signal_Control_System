import tkinter as tk

window = tk.Tk()
window.title("Smart Traffic AI")
window.geometry("500x650")
window.configure(bg="white")

# Title
title = tk.Label(
    window,
    text="SMART TRAFFIC AI",
    font=("Arial", 24, "bold"),
    bg="white"
)
title.pack(pady=20)

# Traffic information
density_label = tk.Label(
    window,
    text="Traffic Density: LOW",
    font=("Arial", 18),
    bg="white"
)
density_label.pack(pady=10)

time_label = tk.Label(
    window,
    text="",
    font=("Arial", 18),
    bg="white"
)
time_label.pack(pady=10)

# Signal canvas
canvas = tk.Canvas(
    window,
    width=180,
    height=400,
    bg="black",
    highlightthickness=0
)
canvas.pack(pady=20)

# Lights
red = canvas.create_oval(40, 30, 140, 130, fill="gray")
yellow = canvas.create_oval(40, 150, 140, 250, fill="gray")
green = canvas.create_oval(40, 270, 140, 370, fill="green")


def green_signal():
    canvas.itemconfig(red, fill="gray")
    canvas.itemconfig(yellow, fill="gray")
    canvas.itemconfig(green, fill="green")

    time_label.config(text="GREEN - 20 seconds")

    window.after(5000, yellow_signal)


def yellow_signal():
    canvas.itemconfig(red, fill="gray")
    canvas.itemconfig(yellow, fill="yellow")
    canvas.itemconfig(green, fill="gray")

    time_label.config(text="YELLOW - 5 seconds")

    window.after(2000, red_signal)


def red_signal():
    canvas.itemconfig(red, fill="red")
    canvas.itemconfig(yellow, fill="gray")
    canvas.itemconfig(green, fill="gray")

    time_label.config(text="RED - 20 seconds")

    window.after(5000, green_signal)


# Start signal
green_signal()

window.mainloop()