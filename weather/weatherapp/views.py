from django.shortcuts import render
from . import views
import requests
from datetime import date
from .models import City
import os
import requests
from io import BytesIO
from django.core.files import File

# Create your views here.
def index(req):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6d14e8c281baa630a7c34f0c8b652de8'
        
        if req.method == "POST":
            city = req.POST['city']
            print(city)
            city_weather = requests.get(url.format(city)).json() 
            #Temperature Conversion
            temp_f = city_weather['main']['temp']  
            temp_c = round(((temp_f - 32) * 5/9),2) 

            #Image Saving from api
            image = city_weather['weather'][0]['icon']      
            image_url = f'http://openweathermap.org/img/wn/{image}.png' 

            response = requests.get(image_url)
            if response.status_code == 200:
                # Save the image to a temporary file
                image_temp = BytesIO(response.content)
                # Create a City instance and save it with the image
                city_instance = City(cityName=city, temp=temp_c)
                city_instance.icon.save(f"{city}_icon.png", File(image_temp))
                # Save the City instance to the database
                city_instance.save()       
            
            #request the API data and convert the JSON to Python data types
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'temp_c': temp_c,
                'wind' : city_weather['wind']['speed'],
                'humidity' : city_weather['main']['humidity'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : image,
                'date': date.today(),
                'error':"No such city"
            }
            url2 ='https://api.openweathermap.org/data/2.5/forecast?q={}&appid=6d14e8c281baa630a7c34f0c8b652de8'
            city_weather1 = requests.get(url2.format(city)).json()
            forecast_list = city_weather1['list']
            
            # Group forecast data by date
            grouped_forecast = {}
#forecast['dt_txt'] retrieves the timestamp from the forecast data.
# split(' ') splits the timestamp into a list of substrings based on the space character.
# [0] accesses the first element of the resulting list, which represents the date part.
            for forecast in forecast_list:
                date_str = forecast['dt_txt'].split(' ')[0]
                if date_str not in grouped_forecast:
                    grouped_forecast[date_str] = {
                        'date': date_str,
                        'temperature': round(((forecast['main']['temp'])-273.15),2),
                        'wind': forecast['wind']['speed'],
                        'humidity': forecast['main']['humidity'],
                        'description': forecast['weather'][0]['description'],
                        'icon': forecast['weather'][0]['icon'],
                    }
            #print("G", grouped_forecast)
            new_forecast =   list(grouped_forecast.values())   
            # Update the 'weather' dictionary with forecast data
            weather['forecast'] = new_forecast[1:]
            weather.update(search())   
            #print(weather) 
        #returns the index.html template
            return render(req,"index.html",weather)
        return render(req,"index.html")
    except KeyError:
        #print("No such city")
        return render(req,"index.html")
    
def search():
    cities = City.objects.all().order_by('-id')[:2]#order_by('-id') orders the entries by the #ID in descending order (most recent first).
    #[:2] limits the result to the first two entries.
    #print(cities)
    weather ={'city_hist':cities}   
    return weather
