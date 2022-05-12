import pyautogui
pyautogui.FAILSAFE = True

#Get info from Excel Document
f = open("C:\\Users\\lazer\\Downloads\\Entries.csv", "r")
person = (f.readline().split(',')) #Garbage Line
person = (f.readline().split(","))

#Start the loop
while (person[0] != "NULL"):
    pass

f.close()