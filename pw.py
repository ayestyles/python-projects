import pyautogui
import random


while True:

    x = random.randint(1,10)
    pyautogui.press('w', interval=x)
    