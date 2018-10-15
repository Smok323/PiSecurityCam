from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('GUTx6RSh3j6ONcJXEaeUoQZKnbKYRx4R/', views.camera, name='website-cam'),
]
