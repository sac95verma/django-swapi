from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status
from .serializers import StarWarsPeopleSerializer, RatingSerializer, TopCharactersSerializer
from .models import StarWarsPeople, Ratings
from rest_framework.decorators import api_view
from .utils import calculate_average_rating
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class ApiResponseListView(generics.ListAPIView):
    queryset = StarWarsPeople.objects.all()
    serializer_class = StarWarsPeopleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)
        
        if search_term:
            queryset = queryset.filter(name__startswith=search_term)

        return queryset

    def get_paginated_response(self, data):
        return Response({
            'total_records': self.paginator.page.paginator.count,
            'data': data
        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def rate(request):
    if request.method == 'POST':
        character_id = request.data.get('character')
        rating = request.data.get('rating')

        try:
            character = StarWarsPeople.objects.get(reference=character_id)
        except StarWarsPeople.DoesNotExist:
            return Response({"error": "Character not found."}, status=status.HTTP_404_NOT_FOUND)

        rating_data = {
            'character': character.id,
            'rating': rating
        }
        serializer = RatingSerializer(data=rating_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'character': character.name,
                'rating': rating
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def top_characters_view(request, count=10):
    try:
        count = int(count)  # Convert count to an integer
    except ValueError:
        return Response({'error': 'Invalid count parameter.'}, status=status.HTTP_400_BAD_REQUEST)

    characters = StarWarsPeople.objects.all()

    # Calculate average rating for each character
    character_data = []
    for character in characters:
        average_rating = calculate_average_rating(character.id)
        character_data.append({
            'character_id': character.id,
            'name': character.name,
            'average_rating': round(average_rating, 2),
        })

    # Sort characters by average rating in descending order
    sorted_characters = sorted(character_data, key=lambda x: x['average_rating'], reverse=True)

    # Return the top n characters
    top_characters = sorted_characters[:count]

    serializer = TopCharactersSerializer(top_characters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)