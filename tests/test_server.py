import network
import socket
from machine import ADC, Pin
import time

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def web_page():
    if adc.read() > 500:
        gpio_state="ON"
    else:
        gpio_state="OFF"
    
    html = """<html><head> <title>ESP Web Server</title>
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <link rel="icon" href="data:,">
              <style>
              html{font-family: Helvetica;
                   display:inline-block;
                   margin: 0px auto;
                   text-align: center;}
              h1{color: #0F3376;
                 padding: 2vh;}
              p{font-size: 1.5rem;}
                .button{display: inline-block;
                        background-color: #e7bd3b;
                        border: none;
                        border-radius: 4px;
                        color: white;
                        padding: 16px 40px;
                        text-decoration: none;
                        font-size: 30px;
                        margin: 2px;
                        cursor: pointer;}
                .button2{background-color: #4286f4;}
            </style>
            </head>
            <body>
                <h1>ESP Web Server</h1> 
                <p>
                    GPIO state: <strong>""" + gpio_state + """</strong>
                </p>
                <p>
                    <a href="/?led=on"><button class="button">ON</button></a>
                </p>
                <p>
                    <a href="/?led=off"><button class="button button2">OFF</button></a>
                </p>
            </body>
            </html>"""
    return html


adc = ADC(Pin(36, Pin.IN))          # create ADC object on ADC pin
# adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width

do_connect("nombre_wifi", "contraseña_wifi")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6:
        print('LED ON')

    if led_off == 6:
        print('LED OFF')

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()