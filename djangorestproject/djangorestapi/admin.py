from django.contrib import admin
from .models import Person, Species


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "birth_year", "eye_color", "species"]


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["name", "classification", "language"]


admin.site.register(Person, PersonAdmin)
admin.site.register(Species, SpeciesAdmin)
