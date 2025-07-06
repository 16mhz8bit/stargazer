from time import sleep
from picamera2 import Picamera2
import datetime

cam = Picamera2()
cam.start()
sleep(2)

try:
    while True:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mooncamera/cam/{timestamp}.jpg"
        cam.capture_file(filename)
        sleep(2)

except KeyboardInterrupt:
    print("Stopped")