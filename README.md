# django-swapi
Swapi API

## Cloning the Repository
Open your Terminal, and type: `$ git clone git@github.com:sac95verma/django-swapi.git`

## Functions
- performs scraping of https://swapi.dev at a configurable interval
- API endpoints to:
  - View the characters information GET`http://localhost:9001/swapi/people`
  - Search the characters information GET`http://localhost:9001/swapi/people?search=lu`
  - Rate the character from 1 to 5 POST`http://localhost:9001/swapi/people/rate`
  - View top n rated characters GET`http://localhost:9001/swapi/people/top-rated/:count`
 
## Setup
- Install python using `brew install python`
- Install virtual env using `pip install pipenv`
- Install the requirements using `pipenv install`
- Run `pipenv shell`
- Once dependencies are updated. Rename the `db.sqlite3.example` to remove .example
- Use `python manage.py migrate` to create the tables
- Use `python manage.py crontab add` to add the crons
- Use `python manage.py runserver 9001` to start the app.

## For running tests
- Run `python manage.py test swapi`

## Architecture
<img width="765" alt="Screenshot 2023-11-25 at 7 03 19 PM" src="https://github.com/sac95verma/django-swapi/assets/20048299/12546301-37d9-4994-95d7-997cb65cc8ea">
