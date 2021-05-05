# main.py

# from lib.MAX30102 import MAX30102
# from utime import ticks_ms

# if __name__ == '__main__':
#     sensor = MAX30102()  # Loads default ESP32 I2C configuration
#     # sensor = ParticleSensor(i2cHexAddress = 0x57)
#     # sensor = ParticleSensor(i2cHexAddress = 0x57, i2c = i2cInstance)

#     print("Setting up sensor.", '\n')
#     # Setup the sensor with default configuration
#     sensor.setup_sensor()
    
#     print("Reading temperature in °C.", '\n')
#     print(sensor.readTemperature())
    
#     print("Start data acquisition from RED & IR registers.", '\n')
#     red_array = list()
#     ir_array = list()
    
#     t_start = ticks_ms()
#     samples_n=0
#     while (True):
#         for FIFO_pointer in range(32):
#             sensor_data = sensor.read_sensor_multiLED(FIFO_pointer)
#             # red_array.append(sensor_data[0])
#             # ir_array.append(sensor_data[1])
#             samples_n=samples_n+1
#             if (ticks_ms()-t_start) > 999:
#                 f_HZ = samples_n/1
#                 samples_n = 0
#                 t_start = ticks_ms()
#                 print("frequency = ",f_HZ)
#                 print(sensor_data[0])
#                 print(sensor_data[1])
        
# from machine import I2C, Pin
# i2c=I2C(sda=Pin(21),scl=Pin(22),freq=20000)
# # i2c = I2C()          # create I2C peripheral at frequency of 400kHz
#                                 # depending on the port, extra parameters may be required
#                                 # to select the peripheral and/or pins to use

# print(i2c.scan())                      # scan for slaves, returning a list of 7-bit addresses


# # i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42


# MAX30100 test program for MicroPython

# Uses library forked from mfitzp/MAX30100, 
# originally developed for Raspberry Pi

# Contact: Rafael Aroca <aroca@ufscar.br>


from machine import Pin
from machine import I2C
import MAX30100
import time

sda=Pin(21)
scl=Pin(22)             
i2c = I2C(scl=scl,sda=sda)

print('Scanning I2C devices...')
print(i2c.scan())

sensor = MAX30100.MAX30100(i2c=i2c, led_current_red=4.4, led_current_ir=4.4)

print('Reading MAX30100 registers...')
print(sensor.get_registers())

sensor.enable_spo2()

print('Reading sensor...')


for count in range(500):  
  sensor.read_sensor()
  print(sensor.ir, sensor.red)  
  time.sleep(0.5)