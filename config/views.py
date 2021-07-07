from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

import requests
from datetime import date
today = date.today()


def index(request):
  if 'boton1' in request.POST:
    lat = request.POST.get('latitud')
    lon = request.POST.get('longitud')
    w = weather_by_latlon(lat, lon)
    print(w)
    return redirect('/success/')
    #context = {'clima': w,}

  
  elif 'boton2' in request.POST:
    ciudad = request.POST.get('ciudad')
    w = weather_by_locations(ciudad)
    #context = {'clima': w,}
    print(w)
  
  elif 'boton3' in request.POST:
    pais = request.POST.get('pais')
    w = weather_by_locations(pais)
    print(w)
    #context = {'clima': w,}

  return render(request, 'index.html')


def weather_by_latlon(lat, lon):

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
  clima_estado = clima['weather_state_name']

  return clima_estado


def weather_by_locations(location):

  # Obtener el woeid por ciudad / pais
  r = requests.get('https://www.metaweather.com/api/location/search/?query=%s'%(location))
  location = r.json()[0]
  woeid = location['woeid']

  # Obtener el estado del clima
  this_date = today.strftime("%Y/%m/%d")
  r = requests.get('https://www.metaweather.com/api/location/%d/%s'%(woeid,this_date ))
  clima = r.json()[0]
  clima_estado = clima['weather_state_name']
  return clima_estado



