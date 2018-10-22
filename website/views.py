from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from . import camera


def home(request):
    return render(request, 'website/home.html')


def cameraview(request):
    # cam = camera.Camera()

    return render(request, 'website/camera.html')
