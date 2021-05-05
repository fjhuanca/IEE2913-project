from machine import ADC, Pin
import time

adc = ADC(Pin(39, Pin.IN))          # create ADC object on ADC pin
# adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_12BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width
while True:
    v = adc.read() / 4095 * 3600 / 10
    print("Valor:", str(v) + "C")
    time.sleep(0.2)