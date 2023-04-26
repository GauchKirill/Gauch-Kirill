import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.cleanup()

maxVol = 3.3
depth = 8
max_adc = 2 ** depth
transition = 0.97

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
GPIO.setup(troyka, GPIO.OUT)
GPIO.output(troyka, 0)

def show_bin_to_leds(value):
    GPIO.output(leds, dec2bin(value))

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
    adc_list = []
    value_transition = transition * max_adc
    adc_value = 0
    while(adc_value == 0):
        adc_value = adc()
        if (adc_value != 0):
            while (adc_value != 0):
                adc_value = adc()
            break
            
    start_time = time.time()
    print(start_time)
    GPIO.output(troyka, 0)
    while (adc_value < value_transition):
        adc_value = adc()
        voltage = maxVol * adc_value / (2 ** depth)
        print("Voltage: {:.2f}, ADC: {:^3}".format(voltage, adc_value))
        show_bin_to_leds(adc_value)
        adc_list.append(adc_value)
    discharge_time = time.time()
    GPIO.output(troyka, 1)
    value_end = (1-transition) * max_adc
    while (adc_value > value_end):
        adc_value =adc()
        voltage = maxVol * adc_value / (2 ** depth)
        print("Voltage: {:.2f}, ADC: {:^3}".format(voltage, adc_value))
        show_bin_to_leds(adc_value)
        adc_list.append(adc_value)
    end_time = time.time()

    measure_data_str = [str(item) for item in adc_list]
    measure_data_str.append(str(start_time))
    measure_data_str.append(str(discharge_time))
    measure_data_str.append(str(end_time))
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(measure_data_str))
    plt.plot(adc_list)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()