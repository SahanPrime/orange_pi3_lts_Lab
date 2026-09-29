#!/usr/bin/env python3
import sys, time
from smbus2 import SMBus, i2c_msg

BUS = int(sys.argv[1]) if len(sys.argv) > 1 else 0   # the bus where i2cdetect showed 38
ADDR = 0x38
LOG = "/var/log/aht10.csv"

def init(bus):
    bus.i2c_rdwr(i2c_msg.write(ADDR, [0xE1, 0x08, 0x00]))  # enable calibration
    time.sleep(0.05)

def read(bus):
    bus.i2c_rdwr(i2c_msg.write(ADDR, [0xAC, 0x33, 0x00]))  # trigger measurement
    time.sleep(0.08)
    for _ in range(10):                                     # poll busy flag
        r = i2c_msg.read(ADDR, 6)
        bus.i2c_rdwr(r)
        d = list(r)
        if not d[0] & 0x80:                                 # bit 7 = busy
            break
        time.sleep(0.01)
    else:
        raise IOError("sensor stayed busy")
    raw_h = (d[1] << 12) | (d[2] << 4) | (d[3] >> 4)
    raw_t = ((d[3] & 0x0F) << 16) | (d[4] << 8) | d[5]
    return raw_t / 2**20 * 200 - 50, raw_h / 2**20 * 100

with SMBus(BUS) as bus:
    init(bus)
    while True:
        try:
            t, h = read(bus)
            line = f"{time.strftime('%F %T')},{t:.2f},{h:.1f}"
            print(line, flush=True)            # goes to the journal
            with open(LOG, "a") as f:
                f.write(line + "\n")
        except Exception as e:
            print("read error:", e, flush=True)
        time.sleep(5)
