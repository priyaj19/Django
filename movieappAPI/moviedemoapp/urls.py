from django.contrib import admin
from django.urls import path
from moviedemoapp import views
urlpatterns = [
    path('', views.movie_list,name='movie_list'),
]
