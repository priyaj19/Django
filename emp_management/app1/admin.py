from django.contrib import admin
from .models import Departments,Employee

# Register your models here.

@admin.register(Departments)
class departmentsAdmin(admin.ModelAdmin):
    list_display=["id","name"]


@admin.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    list_display=["id","name","email","contact","gender","department","salary","image"]