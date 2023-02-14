import machine
from time import sleep_ms
from uPy_APDS9900.apds9900LITE import APDS9900LITE
from machine import Pin

#Init I2C Buss for Sensor 1 on RP2040
i2c_1 =  machine.I2C(1,scl=machine.Pin(7), sda=machine.Pin(6))

#Init I2C Buss for Sensor 2 on RP2040
i2c_2 =  machine.I2C(0,scl=machine.Pin(9), sda=machine.Pin(8))
print(i2c_1.scan(), i2c_2.scan())

apds9900_1=APDS9900LITE(i2c_1)      # Enable the first sensor
apds9900_1.prox.enableSensor()    # Enable Proximity sensing for the first sensor

apds9900_2=APDS9900LITE(i2c_2)      # Enable the second sensor
apds9900_2.prox.enableSensor()    # Enable Proximity sensing for the second sensor

while True:
        sleep_ms(25) # wait for readout to be ready
        #print the proximity values for both sensors
        print('Sensor 1: ', apds9900_1.prox.proximityLevel)
        print('Sensor 2: ', apds9900_2.prox.proximityLevel)
        
        # check the proximity value of the first sensor
        if apds9900_1.prox.proximityLevel > 1000:
            print('Sensor 1: Turn Left')
        elif apds9900_2.prox.proximityLevel > 1000:
            print('Sensor 2: Turn Right')
        elif apds9900_1.prox.proximityLevel < 1000 and apds9900_2.prox.proximityLevel < 1000:
            print('Run')
        else:
            print('Stop')
