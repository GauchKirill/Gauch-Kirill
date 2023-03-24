import RPi.GPIO as GPIO
import time
def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    T = int(input('Введите период:'))
    while True:
        for num in range(2 ** 8):
            time.sleep(T/2 ** 9)
            GPIO.output(dac, dec2bin(num))
            print("V: " + "{:.2f}".format(3.3 * float(num) / 255) + " В")
        for num in range(2 ** 8 - 1, 0, -1):
            time.sleep(T/2 ** 9)
            GPIO.output(dac, dec2bin(num))
            print("V: " + "{:.2f}".format(3.3 * float(num) / 255) + " В")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
