from rest_framework import serializers
from swapi.models import StarWarsPeople

        
# class ListPeopleSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         return {
#             'total_records': len(data),
#             'data': super().to_representation(data),
#         }  

class StarWarsPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarWarsPeople
        fields = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'created', 'edited', 'url', 'films', 'species', 'starships', 'vehicles']
        # list_serializer_class = ListPeopleSerializer
      
