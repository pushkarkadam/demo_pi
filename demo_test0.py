import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    value = ser.readline()
    try:
        voltage = value.decode('utf-8')
    except:
        continue
    print("The voltage is {}".format(voltage))
    time.sleep(0.5)
