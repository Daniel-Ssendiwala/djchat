from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('<str:rm>/',views.room, name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:rm>/',views.getMessages, name='getMessages'),
]
