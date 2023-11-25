import requests
import requests
import json
import re
from swapi.models import StarWarsPeople



SWAPI_BASE_URL = config('SWAPI_BASE_URL', default='')
PAGE_SIZE = 10 #max size available was 10

def ScrapeSwapiPeopleApi():
    page = 1
    has_results = True

    while has_results:
        api_endpoint = f'{SWAPI_BASE_URL}?page={page}'
        response = requests.get(api_endpoint)
        response.raise_for_status()

        json_data = response.json()
        results = json_data.get('results', [])

        if results:
            save_results(results)
            page += 1
        else:
            has_results = False

    print('Successfully fetched and saved data.')

def save_results(results):
    for result in results:
        # Convert the result data to a dictionary with keys matching the model fields
        result_data = {
            'reference': re.findall(r"\d+", result['url'])[0],
            'name': result['name'],
            'birth_year': result['birth_year'],
            'eye_color': result['eye_color'],
            'gender': result['gender'],
            'hair_color': result['hair_color'],
            'height': result['height'],
            'mass': result['mass'],
            'skin_color': result['skin_color'],
            'homeworld': result['homeworld'],
            'films': result['films'],
            'species': result['species'],
            'starships': result['starships'],
            'vehicles': result['vehicles'],
            'url': result['url'],
            'created': result['created'],
            'edited': result['edited'],
        }
        existing_record = StarWarsPeople.objects.filter(reference=result_data['reference']).first()
        if existing_record:
            # Update existing record
            for key, value in result_data.items():
                setattr(existing_record, key, value)
            existing_record.save()
        else:
            people = StarWarsPeople(**result_data)
            people.save()