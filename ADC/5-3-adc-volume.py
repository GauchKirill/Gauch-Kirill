import RPi.GPIO as GPIO
import time

maxVol = 3.3
depth = 8

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac =  [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def volume(value):
    s = 0
    delta = 2 ** depth / depth
    num = 0
    while (num < value):
        num += delta
        s *= 2
        s += 1
    signal = dec2bin(s)
    GPIO.output(leds, signal)

def adc():
    value = 0
    for step in range(depth):
        weight = 2 ** (depth - step - 1)
        value += weight
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.007)
        compValue = GPIO.input(comp)
        if compValue == 0:
            value -= weight
    return value

try:
    while(True):
        value = adc()
        voltage = maxVol * value / (2 ** depth)
        volume(value)
        print("Voltage: {:.2f}, ADC: {:^3}".format(voltage, value))
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()