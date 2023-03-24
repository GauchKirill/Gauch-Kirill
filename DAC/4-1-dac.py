import RPi.GPIO as GPIO
def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while True:        
        num = input()
        if num == 'q':
            exit()
        else:
            try :
                int(num)
            except ValueError:
                print("Error input. Mast be natural number from 0 to 255")
            else:
                num = int(num)
                if num > 255:
                    print("Number mast be from 0 to 255")
                elif num < 0:
                    print("Number mast be >= 0")
                else:
                    GPIO.output(dac, dec2bin(num))
                    print("V: " + "{:.2f}".format(3.3 * float(num) / 256) + " В")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
