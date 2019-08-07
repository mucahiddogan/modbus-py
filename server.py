import argparse
from pyModbusTCP.server import ModbusServer, DataBank
import socket
import sys
import time
import threading
from threading import Thread, Lock
import RPi.GPIO as GPIO
from datetime import datetime
import os

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Host')
    parser.add_argument('-p', '--port', type=int, default=502, help='TCP port')
    args = parser.parse_args()
    server = ModbusServer(host=args.host, port=args.port)

temperature = []
time_now = []
#dizi = []
def threadFunc(c): 
    while 1:
        for i in range(100):
            bits = DataBank.get_bits(0,1)
            temp = os.popen("vcgencmd measure_temp").readline()
            now = datetime.now()
            str_date = now.strftime("%M%S")
            temp = temp.replace("temp=", "").replace("'C\n" , "")
            tempint = int(float(temp))
           
            int_date = int(str_date)
            
            temperature.append(tempint)
            time_now.append(int_date)
            dizi = time_now[i],temperature[i]
            
            time.sleep(1)
            print(dizi, type(dizi))
            
            DataBank.set_words(0, dizi)
            print("bitttts", bits)
            if bits[0] == 1:
                print("1 geldi babba")
                GPIO.output(40, GPIO.HIGH)
            else:
                print("0 geldi babba")
                GPIO.output(40, GPIO.LOW)
        time.sleep(0.25)

thread1 = Thread(target=threadFunc, args=[1,])
thread1.start()
server.start()
