from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2


class Camera:
    def __init__(self):
        self.cam = PiCamera()
        self.cap = PiRGBArray(self.cam)

    def getframe(self):
        self.cam.capture(self.cap, format="BGR")
        image = self.cap.array
        jpeg = cv2.imdecode('.jpeg', image)
        return jpeg.tobytes()
