from django.shortcuts import render
from django.contrib.auth import forms


def home(request):
    return render(request, 'website/home.html')


def cameraview(request):
    return render(request, 'website/camera.html')


def login(request):
    form = forms.AuthenticationForm.as_p()
    if request.POST:
        if form.is_valid():
            return render(request, 'login.html', context=form)
