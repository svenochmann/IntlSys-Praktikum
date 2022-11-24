from machine import Pin
from time import sleep

in1= Pin(26, Pin.OUT)  #in1 coil 4
in2= Pin(25, Pin.OUT)  #in2 coil 2
in3= Pin(33, Pin.OUT)   #in3 coil 3
in4= Pin(32, Pin.OUT)  #in4 coil 1


pins = [in1, in2, in3, in4]

sequenz = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]  

while True:
    for step in sequenz:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(1)