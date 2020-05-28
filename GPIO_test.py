import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 21
print('Reading temperature&humidity')

try:
    while True:
        h,t = dht.read_retry(sensor,pin)
        if h is not None and h is not None:
            print("Temperature = {0:0.1f}C Humidity = {1:0.1f}%".format(t,h))
        else:
            print("Error!")
except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("end of program")    