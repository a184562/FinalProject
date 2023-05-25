import requests
import json

API_KEY = '6d0ab3d5de22afe7d15e2122497294bc'

url = 'https://api.themoviedb.org/3/genre/movie/list?language=ko&api_key='+API_KEY
response = requests.get(url)
gendata = response.text
gen = json.loads(gendata)

gen = gen['genres']