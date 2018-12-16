import serial
ser = serial.Serial('COM4')
print(ser.name)
ser.write(b'hello')
ser.close