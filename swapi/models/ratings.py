from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .peoples import StarWarsPeople

    
class Ratings(models.Model):
    character = models.ForeignKey(StarWarsPeople, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    created = models.DateTimeField(auto_now_add=True, blank=True)
    