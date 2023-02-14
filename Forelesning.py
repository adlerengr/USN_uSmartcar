import machine
from time import sleep_ms
from uPy_APDS9900.apds9900LITE import APDS9900LITE
from machine import Pin


#Init I2C Buss on RP2040
i2c =  machine.I2C(0,scl=machine.Pin(17), sda=machine.Pin(16))

apds9900=APDS9900LITE(i2c)      # Enable sensor
apds9900.prox.enableSensor()    # Enable Proximit sensing


while True:
        sleep_ms(25) # wait for readout to be ready
        print(apds9900.prox.proximityLevel)   #Print the proximity value
        if apds9900.prox.proximityLevel > 1000:
            print('Turn L/R')
        else:
            print('Drive forward')
    
