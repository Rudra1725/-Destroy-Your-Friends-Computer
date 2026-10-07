import webbrowser as wb
import time
import random
import pyautogui as pg

time.sleep(2)

while True:
    pg.moveTo(0, 0,duration = 0.50)
    link = ["Put the Adults Website Or Someething Funny"]
    choice = random.choice(link)
    ime.sleep(1)
    wb.open(choice)
    
