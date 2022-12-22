from machine import Pin
from time import sleep


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

result=[]

seq =[[1,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]


while True:
    for step in seq:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.001)
        trigPIN.value(0)
        sleep(1)
        trigPin.value(1)
        sleep(1)
        trigPin.value(0)
                    
        
        
