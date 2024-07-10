from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    gen = (
        ('male','male'),
        ('female','female'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()
    gender = models.CharField(max_length=50,choices=gen)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="images")