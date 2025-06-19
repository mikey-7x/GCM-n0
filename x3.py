import os
import time
import re

folder_path = "/storage/emulated/0/documents/gcmno"  # ← change to actual log location

def get_latest_file(folder):
    try:
        files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        if not files:
            print("❌ No .txt file found in", folder)
            return None
        latest = max(files, key=lambda x: os.path.getmtime(os.path.join(folder, x)))
        return os.path.join(folder, latest)
    except Exception as e:
        print("❌ Error accessing folder:", e)
        return None

def parse_line(line):
    # Print raw for debug
    print("🧾 RAW:", line.strip())

    # Click format: C:123,456
    if 'C:' in line:
        match = re.search(r'C:(\d+),(\d+)', line)
        if match:
            return int(match.group(1)), int(match.group(2)), "click"

    # Movement format: M: or X= and Y=
    match = re.search(r'[-+]?\d+', line)
    if match:
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        if len(numbers) >= 2:
            return numbers[0], numbers[1], "move"

    return None, None, None

def read_live(file_path):
    print("📡 Listening for data...")
    try:
        with open(file_path, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                x, y, kind = parse_line(line)
                if x is not None and y is not None:
                    if kind == "click":
                        print(f"🖱️  Click → X: {x}, Y: {y}")
                    else:
                        print(f"🕹️  Move  → X: {x}, Y: {y}")
    except Exception as e:
        print("❌ Error reading file:", e)

if __name__ == "__main__":
    path = get_latest_file(folder_path)
    if path:
        print(f"📁 Reading: {path}")
        read_live(path)
    else:
        print("❌ Log file not found.")
