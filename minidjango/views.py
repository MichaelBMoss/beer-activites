import requests
from django.http import HttpResponse
from django.shortcuts import render
from jinja2 import Template



def index(request):
    response = requests.get('https://www.boredapi.com/api/activity?type=recreational')
    data = response.json()
    activity = data['activity']
    beer={}
    response2 = requests.get('https://api.punkapi.com/v2/beers/random')
    data2 = response2.json()
    for beer in data2:
        name=beer['name']
        tagline=beer['tagline']
        description=beer['description']

        
    context = {
        'activity_ph':activity,
        'name_ph':name,
        'tagline_ph':tagline,
        'description_ph':description,
    }
    return render(request, 'index.html', context)
