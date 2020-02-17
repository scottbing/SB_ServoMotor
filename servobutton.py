import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# servo motor
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

#button
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # button

    
while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH: 
         print("Button was pushed!")
    
try:
    while True:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        sleep(1) # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        sleep(1) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        sleep(1) # sleep 1 second 
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
