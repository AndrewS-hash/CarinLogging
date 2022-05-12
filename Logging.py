import pyautogui

RANAME = "Andrew"
RABUILDING = "Cucharas"
RAFLOORNUM = 4
MONTH = "March"
CARINDATE = "03/15/2022"

if (pyautogui.locateOnScreen("Screenshots\\RAName.png")):
    print("RA Name Found!")
    pyautogui.moveTo(pyautogui.locateOnScreen("Screenshots\\RAName.png"))
    pyautogui.move(0, 25)
    pyautogui.leftClick()
    pyautogui.typewrite(RANAME)
else:
    print("Name not found")
    quit()

pyautogui.moveTo(500, 500)
pyautogui.scroll(-300)

if (pyautogui.locateOnScreen("Screenshots\\RABuilding.png")):
    print("RA Building Found!")
    pyautogui.moveTo(pyautogui.locateOnScreen("Screenshots\\RABuilding.png"))
    
else:
    print("Building not found")
    quit()


