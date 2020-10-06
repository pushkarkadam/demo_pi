import time
import serial
import matplotlib.pyplot as plt
import datetime
import sys

if len(sys.argv) != 2:
    print("Usage: python demo_test.py datapoints")
    sys.exit(1)

datapoints = int(sys.argv[1])

ser = serial.Serial('/dev/ttyACM0', 9600)

voltages = []
time_period = []


while len(voltages) <= datapoints:
    value = ser.readline()
    voltage = value.decode('utf-8')
    voltages.append(voltage)
    time_period.append(datetime.datetime.now().strftime('%H:%M:%S'))
    print("The voltage is {}".format(voltage))
    time.sleep(0.5)

fig, ax = plt.subplots()
ax.plot(time_period, voltages)

ax.set(xlabel="time (s)", ylabel="voltage (V)", title="Voltages")
plt.xticks(rotation=45, ha="right")
ax.grid()

fig.savefig("test.png")
plt.show()
