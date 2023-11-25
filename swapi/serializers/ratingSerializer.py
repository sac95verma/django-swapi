from rest_framework import serializers
from swapi.models import Ratings

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['character', 'rating']