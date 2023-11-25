from rest_framework import serializers
from swapi.models import StarWarsPeople

class TopCharactersSerializer(serializers.Serializer):
    character_id = serializers.IntegerField()
    name = serializers.CharField()
    average_rating = serializers.FloatField()