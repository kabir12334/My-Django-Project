from django.contrib import admin
from movieapp.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin) :
       list_display = ['rdate','moviename','hero','herione','rating']
admin.site.register(Movie,MovieAdmin)