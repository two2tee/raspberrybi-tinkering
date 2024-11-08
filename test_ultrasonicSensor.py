from gpiozero import DistanceSensor
from gpiozero import LED
from time import sleep
led = LED(5)
check_frequency_sec = 0.1
dist_threshold = 0.999


ultrasonic = DistanceSensor(echo=19, trigger=26, threshold_distance=dist_threshold)

while True:
    sleep(check_frequency_sec)
    dist = ultrasonic.distance
    print(dist)
    if(dist <= dist_threshold):
        led.on()
    else:
        led.off()
