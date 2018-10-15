from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} logged in!')
    else:
        form = AuthenticationForm()
    return render(request, 'website/home.html', {'form': form})


def camera(request):
    return render(request, 'website/camera.html')

