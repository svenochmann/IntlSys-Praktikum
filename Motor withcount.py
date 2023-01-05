from machine import Pin
from time import sleep
import utime     #Maybe
import csv

"""def"""
#Schickt signal und berechnet es in cm/s (Return Distanz in cm/s)
def disctance():
    counter=0
    disctance=0
    duration=0
    #Gibt signal aus
    trigPIN.value(0)
    utime.sleep(2)
    trigPIN.value(1)
    utime.sleep(10)
    trigPIN.value(0)
    utime.sleep(2)
    #Überprüft wie lange das signal gebracht hat.
    startT = utime.ticks_us()/1000000

    feedbackT = utime.ticks_us()/1000000
    #Berechnet es in cm
    if feedbackT == startT:
        distance = "N/A"
    else:
        duration = feedbackT - startT
        soundSpeed = 34300 # cm/s
        distance = duration * soundSpeed / 2
        distance = round(distance, 1)
    return distance
        
"""Pins"""
#Motor
in1= Pin(32, Pin.OUT)   #in1
in2= Pin(33, Pin.OUT)   #in2  
in3= Pin(25, Pin.OUT)   #in3
in4= Pin(26, Pin.OUT)   #in4   
pins = [in1,in2,in3,in4]
#Sensor
echoPIN = Pin(5, Pin.IN)
trigPIN = Pin(18, Pin.OUT)
"""Declaration"""
#Ergebniss liste
result=list()
#Motor Sequenz
seq =[[1,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]

"""Main"""
while True:   #Eine oder zwei ganze umdreumgen
    for step in seq:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.001)
            if tick == 4 :
                dis =  disctance()              #ounter der nach einer umdrehung disntace benutzt?                 
                result.append(dis)
    tick+=1     

        
for i in result:
    #Add result into the csv doc.