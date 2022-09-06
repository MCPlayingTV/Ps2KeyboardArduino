import serial
import keyboard

ser = serial.Serial("/dev/ttyUSB0",9600,timeout=0.01)
while 1:
   line = ser.readline().decode()
   if line != "":
     if line == "[Del]":
      keyboard.press_and_release("del");
     elif line == "[Enter]":
      keyboard.press_and_release("enter");
     elif line == "[Ctrl]":
      keyboard.press("ctrl");
     elif line == "[Shift]":
      keyboard.press("shift");
     elif line == "[Release]":
      keyboard.release("ctrl");
      keyboard.release("shift");
     else:
       if len(line) == 1:
       
         keyboard.press_and_release(line)
