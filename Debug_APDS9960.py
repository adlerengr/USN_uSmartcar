import machine
i2c =  machine.I2C(0,scl=machine.Pin(9), sda=machine.Pin(8))

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))

    if(device==0x39): # APDS9960 Address = 0x39
        deviceID=i2c.readfrom_mem(devices[0],0x92, 1) #Get deviceID
        deviceID=int.from_bytes(deviceID,'big')       #Conv byte to int
        if(deviceID==0x29):
           deviceID=9900
        elif(deviceID==0x20):
            deviceID=9901
        else:
            deviceID=9960

        print("Found ADPS-",deviceID)