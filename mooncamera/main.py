from time import sleep
from picamera2 import Picamera2
import datetime
from center_moon import distance_from_center

cam = Picamera2()

photo_config = cam.create_still_configuration(
    main={"size": (1920, 1080)},  
    lores={"size": (640, 480)},   # Lower resolution for preview
    display="lores"
)
cam.configure(photo_config)

cam.start()
sleep(2)

try:
    while True:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mooncamera/cam/{timestamp}.jpg"
        cam.capture_file(filename, quality=95)

        # Calculate distance from center
        distance = distance_from_center(filename)
        print(f"Distance from center for {filename}: {distance} pixels")

        sleep(2)

except KeyboardInterrupt:
    print("Stopped")