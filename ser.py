from time import sleep, strftime, time
import serial
import pynmea2
import datetime
#import pyscopg
#import json
import os
#---------------------------------------#
#setup the serial port is connected
#conn = psycopg2.connect(database='mydb', user='user', password='user')
#cur = conn.cursor()
#cur.execute('''select * from port''')
#except psycopg2.Error as e:
#    pass
#conn.commit()
#for row in cur.fetchall():
#    print row[0]
#cur.close()
row = "/dev/ttyS0"
ser = serial.Serial(row, baudrate = 38400, timeout = 0.5)
#--------------------------------------------------------------#
def Initialize():
    global ser
    try:
        ser.isOpen()
        print("\n Serial is open")
    except:
        print ("Error: serial Not Open")
#-------------------------------------------#
def Reader():
    global ser
    if (ser.isOpen()):
        try:
            x = ser.readline()
            if x [0:6] == '$IIMTW'
            parsed_line = pynmea2.parse(x)
            temperature_reading = parsed_line.temperature
            alpha = temperature_reading
            meteo_data=[]
            meteo_data.append(alpha)
            print (meteo_data)
            x = (x)
            return x
        except:
            return "unable to print"
    else:
        return "cannot open serial port"
