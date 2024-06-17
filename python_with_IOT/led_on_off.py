import tkinter as tk
import serial
import time
ser=serial.Serial(port='COM3',baudrate=9600)
switchon="1"
switchoff="2"
def ledon():
    ser.write(bytes(switchon,'utf-8'))
def ledoff():
    ser.write(bytes(switchoff,'utf-8'))
root=tk.Tk()
root.title("Tkinter button return value example")
button=tk.Button(root,text="LED on",command=ledon)
button.pack(pady=10)
button=tk.Button(root,text="LED off",command=ledoff)
button.pack(pady=10)
root.mainloop()
