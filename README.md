# ✨ GCM-n0 (Gesture Control Mouse - Wireless)

[![Arduino](https://img.shields.io/badge/Arduino-IDE-blue?logo=arduino)](https://www.arduino.cc/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://github.com/mikey-7x/GCM-n0/blob/main/LICENSE)
[![Built with Love](https://img.shields.io/badge/Built%20with-%E2%9D%A4-red)](https://github.com/mikey-7x)

> Control your computer mouse with just your **hand gestures** — no wires, no limits!

---
# **👁️‍🗨️Practical outputs**  
[![GCA-n0](https://img.youtube.com/vi/nHxFMHYk4dc/maxresdefault.jpg)](https://youtu.be/nHxFMHYk4dc)

---
## 📦 Components Used

- 🔹 **ADXL345** (Digital Accelerometer)
- 🔹 **HC-05** Bluetooth Module
- 🔹 **Homemade Touch Sensor**
- 🔹 **Arduino Nano** (or compatible board)

---

## ⚡ How It Works

The project allows controlling the cursor and clicks using simple finger gestures:

- **Cursor Movement (Up, Down, Left, Right):**
  - Attach **T1** and **T2** touch sensors on the **first** and **second** fingers (after applying insulation tape).
  - When **first** and **second fingers** are **joined together**, **cursor movement** is activated.
  - Removing the joint **stops** cursor movement.

- **Mouse Clicks:**
  - Attach **T3** touch sensor on the **mid of the second finger**.
  - When **cursor movement is off**:
    - **First finger touching thumb** → **Left Click**
    - **Second finger touching thumb** → **Right Click**

> **Note**: The **common wire** of the touch sensor must be connected to your **body**.
>in **gcm-n0.py** file, make sure add two space at last line of code 



---

## 🛠️ Setup Instructions

### 🔧 Arduino Setup
- Install **Adafruit ADXL345 Sensor** library:
  - Arduino IDE → Library Manager → Search "**Adafruit ADXL345**" → Install.

- Upload the provided `GCM-n0.ino` code to your Arduino board.

### 💻 Python Setup
- Install required Python libraries:
```bash
pip install pynput pyserial
```
(time module is built into Python by default.)

Run the GCM-n0.py script after Bluetooth connection.



---

🖥️ How to Use

1. Power on your Arduino + HC-05 module.


2. Pair HC-05 with your computer via Bluetooth.


3. Run the Python script GCM-n0.py.


4. Use gestures:

➡️ Join first and second fingers → Move cursor

✋ Unjoin fingers → Stop cursor

☝️ Thumb + First finger → Left Click

✌️ Thumb + Second finger → Right Click





---

📸 Project Images

**Circuit Diagram:**

![Circuit Diagram](gcm-n0.jpg)

---

📁 Project Structure

GCM-n0

├── GCM-n0.ino (Accelerometer + Touch Sensors)

├── GCM-n0.py (Mouse Control)

├── Images (Images)

└── README.md

---

# 🪽 bring GCM-n0 readings in termux 

1) download serial bluetooth terminal app from:
   
https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal

2)turn on android's bluetooth and scan, connect 'hc-05' device (default password is 1234),

open serial bluetooth terminal and click three dash at left corner then go:

setting<misc.<save+log folder

choose your accessible folder where logs are saved

3)again go three dash at left corner and choose 'device' option then connect 'hc-05' device 

now you can see GCM-n0 readings in this app

4)click three dot at right corner click the 'data' option and click to 'log'(mark/enable the log)

now logs are saved in your selected path in text form

5)open termux and run:

```
pkg install python -y
```
```
wget https://raw.githubusercontent.com/mikey-7x/GCM-n0/refs/heads/main/x3.py
chmod +x x3.py
```
to see readings run:
```
python x3.py
```

# License

This project is open-source and available under the [MIT License](LICENSE).

---

## **📜 Credits**  
Developed with  ❤️ by **[mikey-7x](https://github.com/mikey-7x)** 🚀🔥  


[other repository](https://github.com/mikey-7x?tab=repositories)

Special thanks to the open-source community for providing awesome libraries!
