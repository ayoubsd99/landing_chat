from django.urls import path,include

from landing.views import rooms,home

urlpatterns = [
    path('', home.HomeView.as_view(),name="home"),
    path('chat/<str:room_name>/', rooms.RoomView.as_view(),name="room"),

]