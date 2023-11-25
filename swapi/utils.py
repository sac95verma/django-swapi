from django.db.models import Avg
from .models import Ratings

def calculate_average_rating(character_id):
    average_rating = Ratings.objects.filter(character_id=character_id).aggregate(Avg('rating'))['rating__avg']
    # Return 0 if there are no ratings yet
    return average_rating or 0  