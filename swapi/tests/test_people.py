import os
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

HEADERS = {'HTTP_AUTHORIZATION': 'Token your_secret_token'}

class PeopleApiTest(TestCase):
    fixtures = ['swapi/tests/fixtures/peoples.json']
    
    def setUp(self):
        self.client = APIClient()
        
    def test_people_api_with_search_param(self):
        url = reverse('swapi:api-data-list') + '?search=Luke'
        response = self.client.get(url, **HEADERS)
        jsonData = response.json()
        expected_structure = {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "https://swapi.dev/api/people/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ]
        } 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(jsonData['total_records'], 1)
        self.assertEqual(jsonData['data'], [expected_structure])

    
    def test_people_api_with_invalid_search_param(self):
        url = reverse('swapi:api-data-list') + '?search=InvalidName'
        response = self.client.get(url, **HEADERS)
        jsonData = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(jsonData['total_records'], 0)
        self.assertEqual(len(jsonData['data']), 0)