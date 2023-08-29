import requests 
from gpiozero import LED,Button
from time import sleep
from signal import pause

led = LED(18)
button = Button(17)

def url():
    url1= 'https://maker.ifttt.com/trigger/Notify/json/with/key/jLExtJZ9wFvUdcOaTpbmAijNNUaMcm7sr-ZoUnqpjMV'
    r = requests.get(url1)
    led.on()
    sleep(2)
    print(r.status_code)
    led.off()
    return r


button.when_pressed = url

pause()