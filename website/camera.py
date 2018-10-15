import cv2

# Will have to be modified to Access Raspberry Pi Camera Module


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.ret, self.frame = self.cap.read()

    def __del__(self):
        self.cap.release()

    def getframe(self):
        ret, frame = self.cap.read()
        ret, jpeg = cv2.imdecode('.jpeg', frame)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.ret, self.frame = self.cap.read()

