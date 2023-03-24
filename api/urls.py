from django.urls import path
from .views import RoomView

# from .views import main

urlpatterns = [
    path("room/", RoomView.as_view()),
]
