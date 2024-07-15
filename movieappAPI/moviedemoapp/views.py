from django.shortcuts import render

# Create your views here.

from .data_loader import load_movie_data 

def movie_list(request):
    movie_data=load_movie_data()
    return render(request,'movie_list.html',{'movies':movie_data})