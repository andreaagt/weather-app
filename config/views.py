from django.conf import settings
from django.shortcuts import render, redirect
from django.template import Context, Template

import requests
from datetime import date
today = date.today()

def index(request):
  if 'boton1' in request.POST:
    lat = request.POST.get('latitud')
    lon = request.POST.get('longitud')
    w = weather_by_latlon(lat, lon)
    if w != None:
      context = {'clima': w['weather_state_name'], 'humedad': w['humidity'],
      'temp_min': w['min_temp'], 'temp_max': w['max_temp']}
      return render(request, 'clima.html', context)
    else:
      return render(request, 'not_found.html', {'msg':'Ciudad no encontrada'})
  
  elif 'boton2' in request.POST:
    location = request.POST.get('location')
    w = weather_by_locations(location)
    if w != None:
      context = {'clima': w['weather_state_name'], 'humedad': w['humidity'],
      'temp_min': w['min_temp'], 'temp_max': w['max_temp']}
      return render(request, 'clima.html', context)
    else:
      return render(request, 'not_found.html', {'msg':'Ciudad no encontrada'})

  return render(request, 'index.html')


def weather_by_latlon(lat, lon):
  try:
  # Obtener el woeid por latitud y longitud
    latt = lat
    long = lon
    r = requests.get('https://www.metaweather.com/api/location/search/?lattlong=%s,%s'%(latt, long))
    location = r.json()[0]
    woeid = location['woeid']

    # Obtener el estado del clima
    this_date = today.strftime("%Y/%m/%d")
    r = requests.get('https://www.metaweather.com/api/location/%d/%s'%(woeid,this_date ))
    clima = r.json()[0]

  except: 
    clima = None
  
  return clima

def weather_by_locations(location):
  try:
    # Obtener el woeid por ciudad / pais
    r = requests.get('https://www.metaweather.com/api/location/search/?query=%s'%(location))
    location = r.json()[0]
    woeid = location['woeid']

    # Obtener el estado del clima
    this_date = today.strftime("%Y/%m/%d")
    r = requests.get('https://www.metaweather.com/api/location/%d/%s'%(woeid,this_date ))
    clima = r.json()[0]

  except: 
    clima = None

  return clima  


