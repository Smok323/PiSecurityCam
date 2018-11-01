from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseServerError
from . import picam

cam = picam.Camera()


def home(request):
    return render(request, 'website/home.html')


def gen(camera):
    while True:
        frame = camera.getframe()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def cameraview(request):
    try:
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")
