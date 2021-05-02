from machine import ADC, Pin
import time

adc = ADC(Pin(36, Pin.IN))          # create ADC object on ADC pin
# adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width
while True:
    print("Valor:", adc.read())
    time.sleep(0.2)