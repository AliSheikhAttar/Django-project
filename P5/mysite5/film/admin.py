from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Movie

admin.site.register(Movie)
