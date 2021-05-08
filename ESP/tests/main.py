from machine import ADC, Pin
import time
# f1 = Pin(32, Pin.IN)
# f2 = Pin(33, Pin.IN)
adc = ADC(Pin(36, Pin.IN))          # create ADC object on ADC pin
# adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_12BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width
while True:
    v = adc.read()
    if  False:
        print("!")
    else:
        # print("low:" + str(0) + ",Audio:"+str(v)+",high:"+str(4095))
        print("Audio:"+str(v))
    # time.sleep(0.001)