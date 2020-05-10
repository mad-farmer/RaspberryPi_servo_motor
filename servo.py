import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
#Disable warnings

GPIO.setmode(GPIO.BOARD)
#GPIO numbering mode

GPIO.setup(11,GPIO.OUT)
# Set pin 11 as an output,

servo1 = GPIO.PWM(11,50)
# pin 11 for servo1, pulse 50Hz

servo1.start(0)
# Start PWM running with value 0


while True:
     
    angle = input("'q' for exit\nEnter angle between 0-180: ")
    #Ask user for angle
    
    if angle=='q': #if angle is q quit the program and clean up
        servo1.stop()
        GPIO.cleanup()
        print("GPIO Clean up")
        break 
    
    else: #turn servo to angle
        angle=float(angle)
        servo1.ChangeDutyCycle(2+angle/18)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

        
        
        
        

