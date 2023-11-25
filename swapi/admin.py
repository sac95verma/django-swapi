from django.contrib import admin

# Register your models here.

from .models import StarWarsPeople, Ratings

admin.site.register(StarWarsPeople)
admin.site.register(Ratings)