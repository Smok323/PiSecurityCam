from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('GUTx6RSh3j6ONcJXEaeUoQZKnbKYRx4R/', views.cameraview, name='website-cam'),
]
