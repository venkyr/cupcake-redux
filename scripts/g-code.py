''' Use Python 3 '''
import serial
import io

conn = serial.Serial('/dev/tty.usbmodem1411', 115200, timeout=1, xonxoff=True, rtscts=True)
z = 0

def read():
    while (True):
        s = conn.readline().decode()
        if (s == ''):
            break
        print(s, end='')
        
def send(cmd):
    conn.write(str.encode(cmd+'\r'))
    read()

def up(dist=10):
    global z
    z = z+dist
    send('G1 Z'+str(z))

def dn(dist=10):
    global z
    z = z-dist
    send('G1 Z'+str(z))

def heat(temp=200):
    send('M104 S'+str(temp))

def temp():
    send('M105')

def pos():
    send('M114')


