import pyautogui
import time

# Set the interval for moving the mouse cursor (in seconds)
interval = 300  # 5 minutes

while True:
    # Move the mouse cursor slightly
    pyautogui.moveRel(1, 0)

    # Wait for the specified interval
    time.sleep(interval)
    