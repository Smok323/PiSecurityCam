from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def cameraview(request):
    return render(request, 'website/camera.html')

