from django.contrib import admin
from .models import Game


# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "play_instruction", "version", "per_person_cost"]


admin.site.register(Game, GameAdmin)
