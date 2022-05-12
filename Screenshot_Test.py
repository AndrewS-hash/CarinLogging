import pyautogui

pyautogui.FAILSAFE = True

if pyautogui.confirm("Is the page on the screen?") == "OK":
    pyautogui.moveTo(15,15)
    pyautogui.sleep(1)
    print(pyautogui.locateOnScreen('Carins\\Screenshots\\Name.png'))

