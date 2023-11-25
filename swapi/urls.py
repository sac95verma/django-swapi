from django.urls import path
from .views import ApiResponseListView, rate, top_characters_view

app_name = 'swapi'
urlpatterns = [
    path('people/rate', rate, name='ratings-api'),
    path('people/', ApiResponseListView.as_view(), name='api-data-list'),
    path('people/top-rated/<int:count>/', top_characters_view, name='top-rated-api'),
]
