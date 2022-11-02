import pyautogui
import time
time.sleep(2)
count = 0
times = int( input("Enter how many times do you want to refresh :"))
pyautogui.hotkey('win', 'm')
while count<=times:
    pyautogui.rightClick(x=1250,y=100)
    for i in range(3):
        pyautogui.press("down")
        i+=1
    pyautogui.press("enter")
    count+=1