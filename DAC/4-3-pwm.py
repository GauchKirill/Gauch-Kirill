import RPi.GPIO as GPIO
import time
def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]
GPIO.setmode(GPIO.BCM)
GPIO.setup([15, 24, 25], GPIO.OUT)
GPIO.output(25, 1)
try:
    p = GPIO.PWM(15, 1000)
    s = GPIO.PWM(24, 1000)
    while True:
        d = input('Введите коэффициент заполнения:')
        if int(d):
            d = int(d)
            if (d < 0) | (d > 100):
                print("d mast be from 0 by 100")
            else:
                p.start(d)
                s.start(d)
                print("V:" + "{:.2f}".format(d / 100 * 3.3) + " В")
                time.sleep(5)
                p.stop()
                s.stop()
        else:
            print("d mast be natural number")
    
finally:
    GPIO.cleanup()

