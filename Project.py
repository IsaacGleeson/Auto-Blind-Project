import gpiozero
import time
import datetime
from tkinter import *
import tkinter.font
from random import randint

#Pin allocation
Backward = gpiozero.OutputDevice(18)
Forward = gpiozero.OutputDevice(23)

SpeedPWM = gpiozero.PWMOutputDevice(24)

# GUI Configerations
win = Tk()
win.title("Blind interface")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#variables
now = datetime.datetime.now()
length = 5 #This variable will need to be measured by time taken (in seconds) for the blind to go from the top to the bottom
for x in range(1):
    valueX = randint(5, 9)
for y in range(1):
    valueY = randint(18, 21)

def Time():
    while True:
        if datetime.time(hour=7) < now.time() < datetime.time(hour=19):
            Backward.on()
            Forward.off()
        else:
            Backward.off()
            Forward.on()
        speedFlag = float(500)
        SpeedPWM.value = speedFlag/1000
        time.sleep(length)    
        SpeedPWM.value = 0
        break

def Away():
    while True:
        if datetime.time(hour=valueX) < now.time() < datetime.time(hour=valueY):
            Backward.on()
            Forward.off()
        else:
            Backward.off()
            Forward.on()
        speedFlag = float(500)
        SpeedPWM.value = speedFlag/1000
        time.sleep(length)    
        SpeedPWM.value = 0
        break

def CustomUp():
    while True:
        Backward.on()
        Forward.off()
        speedFlag = float(500)
        SpeedPWM.value = speedFlag/1000
        time.sleep(5)    
        SpeedPWM.value = 0
        break

def CustomDown():
    while True:
        Backward.off()
        Forward.on()
        speedFlag = float(500)
        SpeedPWM.value = speedFlag/1000
        time.sleep(5)    
        SpeedPWM.value = 0
        break

# Widgets
timeButton = Button(win, text = 'Time profile', font = myFont, command = Time, bg = 'blue', height = 1, width = 24)
timeButton.grid(row=0, column=1)

awayButton = Button(win, text = 'Away profile', font = myFont, command = Away, bg = 'blue', height = 1, width = 24)
awayButton.grid(row=1, column=1)

customUpButton = Button(win, text = 'Up', font = myFont, command = CustomUp, bg = 'green', height = 1, width = 24)
customUpButton.grid(row=2, column=1)

customDownButton = Button(win, text = 'Down', font = myFont, command = CustomDown, bg = 'green', height = 1, width = 24)
customDownButton.grid(row=3, column=1)

