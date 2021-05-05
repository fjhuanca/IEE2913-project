# import urequests
import network
from machine import ADC, Pin
import utime
import urequests
import json
def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


# url = 'iee2913-project.herokuapp.com'
# import socket
# def http_get(url):
#     host, path = url.split('/', 1)
#     s = socket.socket()
#     s.connect((host, 80))
#     # request=bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8')	
#     print("Requesting /%s from host %s\n" % (path, host))
#     # s.send(request)
#     s.send(b'GET /messages?id1=2021 HTTP/1.0\r\n\r\n')    
#     dump_socket(s)    
# # print(socket.getaddrinfo(url, 80))

# def dump_socket(s):
#     try:
#         while True:
#             data = s.recv(100)
#             if data:
#                 print(str(data, 'utf8'), end='')
#             else:
#                 print('')  # end with newline
#                 s.close()
#                 break
#     except:
#         s.close()
#         raise

# print(http_get(url+"/"))


do_connect("wifi_ssid", "clave_wifi")

adc_temp = ADC(Pin(35, Pin.IN))
adc_temp.atten(ADC.ATTN_11DB)
adc_temp.width(ADC.WIDTH_12BIT)

adc_bs = ADC(Pin(34, Pin.IN))
adc_bs.atten(ADC.ATTN_11DB)
adc_bs.width(ADC.WIDTH_12BIT)

adc_mic = ADC(Pin(36, Pin.IN))
adc_mic.atten(ADC.ATTN_11DB)
adc_mic.width(ADC.WIDTH_12BIT)

url = "http://iee2913-project.herokuapp.com/data"
headers = {'X-AIO-Key': 'xxxxxxxxxxxxxxxxxxx',
           'Content-Type': 'application/json'}

while True:
    temp = adc_temp.read() / 4096 * 3600 / 10
    bs = adc_bs.read()
    mic = adc_mic.read()
    try:
        data = json.dumps({"temp": temp,
                           "mic": mic,       
                           "bs": bs})
        response = urequests.post(url=url,
                                  headers=headers,
                                  data=data)
        # print("done")
        response.close()
    except:
        print("net error")
    # print(temp)
    # print(bs)
    utime.sleep_ms(25)
