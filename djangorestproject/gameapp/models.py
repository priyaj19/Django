from django.db import models

# Create your models here.


class Game(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    play_instruction = models.TextField()
    version = models.IntegerField()
    per_person_cost = models.DecimalField(max_digits=10, decimal_places=2)
