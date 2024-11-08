from gpiozero import GPIODevice
from time import sleep

ir = GPIODevice(26)
check_frequency_sec = 0.1

while True:
    sleep(check_frequency_sec)
    dist = ir.value
    print(dist)
