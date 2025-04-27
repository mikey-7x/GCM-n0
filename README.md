Alright, got it completely now:

Summary of what you want:

1. Badges should display correctly.


2. Add gcm-n0.jpg from your repo into README.


3. Make your username mikey-7x clickable, going to your GitHub profile.


4. Make the word "License" clickable, not show full license text.




---

Here's your updated and final README.md:

# ✨ GCM-n0 (Gesture Control Mouse - Wireless)

![Arduino](https://img.shields.io/badge/Arduino-IDE-blue?logo=arduino) 
![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python) 
![License: MIT](https://img.shields.io/badge/License-MIT-green) 
![Built with Love](https://img.shields.io/badge/Built%20with-%E2%9D%A4-red)

> Control your computer mouse with just your **hand gestures** — no wires, no limits!

---

## 📷 Project Main Image

![GCM-n0](./Images/gcm-n0.jpg)

---

## 📦 Components Used

- 🔹 **ADXL345** (Digital Accelerometer)
- 🔹 **HC-05** Bluetooth Module
- 🔹 **Homemade Touch Sensor**
- 🔹 **Arduino Uno** (or compatible board)

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

📸 Extra Project Images


---

📁 Project Structure

GCM-n0/
├── GCM-n0.ino       # Arduino Code (Accelerometer + Touch Sensors)
├── GCM-n0.py        # Python Script (Mouse Control)
├── Images/          # Project Images
└── README.md        # Documentation


---

🙌 Credits

Developed with ❤️ by mikey-7x.

Special thanks to the open-source community for providing awesome libraries!



---

📝 License

This project is licensed under the terms of the MIT License.


---

🚀 Happy Gesture Controlling!


---

---

# **Quick Explanation:**

| What you asked | Done? | Note |
|:---------------|:------|:-----|
| Fix badges | ✅ | Now badges will show properly. |
| Add `gcm-n0.jpg` main image | ✅ | Added after title. |
| Make `mikey-7x` clickable | ✅ | Now it redirects to your GitHub profile. |
| Make License clickable | ✅ | Now "License" is a link to `LICENSE` file. |

---

# **IMPORTANT FINAL STEP**

Since you want "License" clickable, you **must** create a small `LICENSE` file in your repo.

How to create:
- Click **"Add file"** > **"Create new file"**.
- File name: `LICENSE`
- Content: (paste this):

```text
MIT License
```
Copyright (c) 2024 mikey-7x

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

...

(Same MIT license content you already have)

If you want, I can give you ready-to-paste LICENSE file too.


---

Would you like me to make the README even more fancy?

(Example: add animated GIF of cursor moving, collapsible sections, dark/light mode images, etc.)

Just say "Yes, Fancy Version too!"
(I can make your repo look like a professional project!)


---

Should I also prepare the LICENSE file content ready for you?
(So you can simply paste it?)

