from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Pet)
class PetAdmin (admin.ModelAdmin):
    list_display = [ 'name', 'species', 'breed', 'age', 'sex' ]

