import serial

with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = 'COM4'
    ser.open()
    ser.write(b'hello')