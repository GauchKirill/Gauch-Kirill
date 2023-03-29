import RPi.GPIO as GPIO
import time

maxVol = 3.3
depth = 8

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def adc():
   for num in range((2**depth)):
       signal = dec2bin(num)
       GPIO.output(dac, signal)
       time.sleep(0.007)
       compValue = GPIO.input(comp)
       if compValue == 0:
           return num

try:
    while(True):
        value = adc()
        voltage = maxVol * value / (2 ** depth)
        print("Voltage: {:.2f}, ADC: {:^3}".format(voltage, value))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()