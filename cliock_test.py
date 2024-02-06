import pyautogui
import time
time.sleep(5)
def clickable():

    x = 1800
    y = 570

    # Move cursor to (x, y) coordinates and click
    pyautogui.moveTo(x, y, duration=1)  # Replace x and y with desired coordinates
    pyautogui.click()

    x = 880
    y = 490
    # Move cursor to (x, y) coordinates and click
    pyautogui.moveTo(x, y, duration=1)  # Replace x and y with desired coordinates
    pyautogui.click()