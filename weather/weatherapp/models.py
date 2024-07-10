from django.db import models

# Create your models here.
class City(models.Model):
    cityName = models.CharField(max_length=50)
    temp = models.IntegerField()
    icon = models.ImageField(upload_to="pics",default="")
    
    def __str__(self): #show the actual city name on the dashboard
        return f"{self.cityName} {self.temp}"