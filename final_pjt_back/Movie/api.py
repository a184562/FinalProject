import requests
import json

API_KEY = '6d0ab3d5de22afe7d15e2122497294bc'
ans = []
for i in range(1,21):
    URL = f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&sort_by=popularity.desc&api_key='+API_KEY
    response = requests.get(URL)
    resdata = response.text
    objs = json.loads(resdata)
    objs = objs['results']
    ans.append(objs)
