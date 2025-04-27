import serial
from pynput.mouse import Controller, Button
import time

mouse = Controller()
port = "COM6"  # Replace with your HC-05 port
baud = 9600
cursor_speed = 1.5
prev_left = 0
prev_right = 0

def connect_serial():
    while True:
        try:
            ser = serial.Serial(port, baud, timeout=0.1)
            print("[✓] Connected to", port)
            time.sleep(2)
            return ser
        except serial.SerialException:
            print("[!] Waiting for Bluetooth reconnection...")
            time.sleep(2)

ser = connect_serial()

while True:
    try:
        line = ser.readline().decode(errors='ignore').strip()
        if not line:
            continue

        if line.startswith("M:"):  # Movement
            try:
                data = line[2:].split(",")
                x = int(data[0])
                y = int(data[1])
                if x != 0 or y != 0:
                    mouse.move(x * cursor_speed, -y * cursor_speed)
            except:
                continue

        elif line.startswith("C:"):  # Clicks
            try:
                data = line[2:].split(",")
                left = int(data[0])
                right = int(data[1])

                if left == 1 and prev_left == 0:
                    mouse.press(Button.left)
                elif left == 0 and prev_left == 1:
                    mouse.release(Button.left)

                if right == 1 and prev_right == 0:
                    mouse.press(Button.right)
                elif right == 0 and prev_right == 1:
                    mouse.release(Button.right)

                prev_left = left
                prev_right = right
            except:
                continue

    except serial.SerialException:
        print("[!] Lost connection. Reconnecting...")
        ser.close()
        ser = connect_serial()
    except KeyboardInterrupt:
        print("Stopped by user.")
        break
