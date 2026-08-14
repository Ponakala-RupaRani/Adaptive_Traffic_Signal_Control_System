# 🚦 Smart Traffic AI

## AI-Based Four-Way Traffic Management System

Smart Traffic AI is a prototype system that analyzes traffic at a four-way intersection and helps determine traffic density and adaptive green-signal timing.

## ✨ Features

- 🚗 Vehicle detection using YOLO
- 🛣️ Four-way traffic analysis
- 📊 NORTH / EAST / SOUTH / WEST traffic counts
- 🚦 Traffic density classification
- ⏱️ Adaptive green-signal timing
- 🧠 Traffic-priority detection
- 🎥 Real-time video demonstration

## 🧠 How It Works

1. Traffic video is provided as input.
2. Vehicles are analyzed from the video.
3. Traffic is divided into four directions:
   - NORTH
   - EAST
   - SOUTH
   - WEST
4. Traffic density is calculated.
5. The direction with higher traffic receives a longer green signal.
6. Lower-traffic directions receive shorter green times.

## 📊 Example

| Direction | Vehicles | Density | Green Time |
|---|---:|---|---:|
| NORTH | 3 | MEDIUM | 30 sec |
| EAST | 4 | MEDIUM | 30 sec |
| SOUTH | 5 | HIGH | 45 sec |
| WEST | 2 | LOW | 20 sec |

### 🚦 Smart Signal Decision

**Highest Traffic:** SOUTH  
**Priority:** SOUTH  
**Green Signal:** 45 seconds

## 🛠️ Technologies

### Technology Stack – Smart Traffic AI

**Frontend**

* **Streamlit** – Used to build the web dashboard/interface.
* Displays:

  * North, East, South, and West vehicle counts
  * Traffic density
  * Green signal timing
  * Video upload and display

**Backend**

* **Python** – Main programming language used for traffic calculations and signal-control logic.
* **YOLO (Ultralytics)** – Used for vehicle detection, including cars, motorcycles, buses, and trucks.
* **OpenCV** – Used for video processing, reading video frames, and drawing bounding boxes.
* **ByteTrack** – Used to track vehicles across multiple video frames and maintain consistent vehicle IDs.


## 📁 Project Files

- `dashboard.py` — dashboard
- `four_way.py` — four-way traffic demo
- `traffic_signal.py` — traffic signal logic
- `traffic.mp4` — demonstration video
- `requirements.txt` — Python dependencies

## ⚠️ Note

This is a prototype/demo system intended to demonstrate AI-assisted traffic management. Vehicle counts may vary depending on video quality and detection accuracy.

## 👩‍💻 Project

**Smart Traffic AI**  
Created by **Ponakala RupaRani**
