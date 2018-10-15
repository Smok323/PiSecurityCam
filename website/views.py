from django.middleware import gzip
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import StreamingHttpResponse
from . import camera


def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} logged in!')
    else:
        form = AuthenticationForm()
    return render(request, 'website/home.html', {'form': form})


cam = camera.Camera()


def gen(cam):
    while True:
        frame = cam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def cameraview(request):
    try:
        return StreamingHttpResponse(gen(camera.Camera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

    return render(request, 'website/camera.html')
