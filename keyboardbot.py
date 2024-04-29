import pyautogui
import time
time.sleep(4)
count=0
while count<=0:
  pyautogui.typewrite("light off")
  pyautogui.press("enter")
  count = count+1
  