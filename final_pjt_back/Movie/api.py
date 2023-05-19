import requests
import json

API_KEY = '6d0ab3d5de22afe7d15e2122497294bc'

URL = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key='

headers = {
    "accept": "application/json",
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZDBhYjNkNWRlMjJhZmU3ZDE1ZTIxMjI0OTcyOTRiYyIsInN1YiI6IjYzZDMxYWQ1ZTcyZmU4MDA4ZTYxNzk1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SueboJ3Wx8JtIIXpLxhgRZus-ODe46tblo54LM_z8vU"
}

response = requests.get(URL+API_KEY, headers=headers)

print(response.text)