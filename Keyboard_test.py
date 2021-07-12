#!/opt/anaconda3/envs/seminar/bin/python

import keyboard
import pyautogui

while True:
    if keyboard.is_pressed('x'):
        break
    elif keyboard.is_pressed('enter'):
        pyautogui.click()
    elif keyboard.is_pressed('w'):
        pyautogui.move(0, -75, 0.5)
    elif keyboard.is_pressed('a'):
        pyautogui.move(-75, 0, 0.5)
    elif keyboard.is_pressed('s'):
        pyautogui.move(0, 75, 0.5)
    elif keyboard.is_pressed('d'):
        pyautogui.move(75, 0, 0.5)
    elif keyboard.is_pressed('up'):
        pyautogui.move(0, -200, 0.5)
    elif keyboard.is_pressed('left'):
        pyautogui.move(-200, 0, 0.5)
    elif keyboard.is_pressed('down'):
        pyautogui.move(0, 200, 0.5)
    elif keyboard.is_pressed('right'):
        pyautogui.move(200, 0, 0.5)