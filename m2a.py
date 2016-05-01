"""
Cos waveshaping synthesis.

"""
from pyo import *
import math
import serial
import threading

DEVICE="/dev/ttyACM3"

S = serial.Serial(DEVICE, 9600, timeout=2)

s = Server(sr=44100, nchnls=2, duplex=0).boot()

### Controls ###
drv = Sig(0)
drv.ctrl(title="Drive")
phi = Sig(0, mul=math.pi/2)
phi.ctrl(title="Odd harmonics <----> Even harmonics")
frs = Sig([40.04,39.41,41.09,38.7])
frs.ctrl([SLMap(10., 1000., 'log', 'value', frs.value)], title="Input osc frequencies")

def worker():
    while True:
        global drv, phi
        y, r, p = map(lambda x: float(x),
            S.readline().strip().replace("\x00", "").split("|"))
        print ((y + 180.0)  / 360.0)
        print (r + 90.0) / 180.0,
        print y
        print r,
        drv.setValue( (y + 180.0)  / 360.0 )
        phi.setValue( (r + 90.0) / 180.0 )
        time.sleep(0.1)

T = threading.Thread(target=worker)

# Amplitude and phase scaling
amp = drv * 2 * math.pi + 0.5
phiscl = Scale(phi, inmin=0, inmax=math.pi/2, outmin=1, outmax=.5)

# Amplitude envelope
f = Linseg([(0,0),(.5,0),(1,1)], mul=amp).play()

# Signal with lot of harmonics
t = HarmTable([1,0,0,0,0,.33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,.2,0,0,0,0,0,0,0,.143])
a = OscBank(t, freq=frs, spread=.0001, slope=1, num=24, fjit=True, mul=f)

# Cos waveshaping
b = Cos(math.pi * a + phi)
b1 = DCBlock(b*phiscl)
c = Sig(b1 / amp, mul=.2).out()
   
s.start()
T.start()
s.gui(locals())



