import matplotlib.pyplot as plt
import serial
import time

ser = serial.Serial('COM4',9600)
time.sleep(2)
emg_list = []

for i in range(100):
    serial_data = ser.readline()
    emg_val = serial_data * (20 / 1023.0)
    emg_val = float(emg_val.decode().strip())
    print(emg_val)
    emg_list.append(emg_val)
    time.sleep(0.1)

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Emg_val')
plt.title('Emg Readings vs. Time for 10 seconds')
plt.show()
    
    
