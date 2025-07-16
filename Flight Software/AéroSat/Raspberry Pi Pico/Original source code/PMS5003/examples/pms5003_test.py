import time
from pms5003 import PMS5003

print("""pms5003_test.py - Continously print all data values.
""")


# Configure the PMS5003 for Enviro+
pms5003 = PMS5003(
    uart=machine.UART(1, tx=machine.Pin(8), rx=machine.Pin(9), baudrate=9600),
    pin_enable=machine.Pin(19),
    pin_reset=machine.Pin(18),
    mode="active"
)

print("config done")


while True:
    data = pms5003.read()
    print(data)
    print("done")
    time.sleep(1.0)
