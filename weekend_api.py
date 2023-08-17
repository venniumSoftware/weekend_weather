import flask
from flask import Flask, request
from werkzeug.wrappers import Request, Response
import json
from datetime import datetime
import requests
from jsonpath_ng import jsonpath, parse

app = Flask(__name__)

appid = 'c878dea49693710ee047f0d71fa610f4'

def kelvinToFahrenheit(kelvin):
    return round(kelvin * 1.8 - 459.67, 2)


### This function uses an input lat and long to get weather data from openweathermap.org 
### It returns data from their free geocode api
def getGeoData(input_zip):
  # api-endpoint
  geo_api_url  = "https://api.openweathermap.org/geo/1.0/zip"
 
  # location given here
  location = str(input_zip) + ",US"
 
  # defining a params dict for the parameters to be sent to the API
  params_geo = {'zip':location, 'appid':appid}
 
  # sending get request and saving the response as response object
  r = requests.get(url = geo_api_url, params = params_geo)
 
  # extracting data in json format
  geo_data = r.json()
  
  return geo_data
  
  


### This function uses an input lat and long to get weather data from openweathermap.org 
### It returns data from their free api  
def getWeatherData(latitude, longitude):
  units = 'standard'

  weather_api_url = 'https://api.openweathermap.org/data/2.5/forecast'
  # defining a params dict for the parameters to be sent to the API
  params_weather = {'lat':latitude, 'lon':longitude, 'units':units, 'appid':appid}
 
  # sending get request and saving the response as response object
  r = requests.get(url = weather_api_url, params = params_weather)
 
  # extracting data in json format
  weather_data = r.json()
  
  if weather_data['cod'] != "200":
      return None
  else:
    jsonpath_list = parse('list[*]')
    weather = jsonpath_list.find(weather_data)
    return weather
  



@app.route("/")
def call_weather_api():

    
  api_key = request.args.get('api_key')
  if (api_key == "3953572e-ffed-453a-bd48-80dd5efb3d27"):
      zipcode = request.args.get('zipcode')
      
      geo_data = getGeoData(zipcode)
        
      if(zipcode != None):
        latitude = geo_data['lat']
        longitude = geo_data['lon']
        
        weather = getWeatherData(latitude, longitude)
        
        if(weather != None):
          date_fixed = []
          temp = []
          feels_like = []
          temp_min = []
          temp_max = []
          pressure = []
          sea_level = []
          grnd_level = []
          humidity = []
          temp_kf = []
          weather_forcast = []
          weather_description = []
          clouds = []
          wind = []
          visibility = []
          pop = []
          rain = []


          for list_obj in weather:
    
              if('dt' in list_obj.value):
                  date_fixed.append(datetime.fromtimestamp(list_obj.value['dt']))
    
              if('main' in list_obj.value):
                  temp.append(kelvinToFahrenheit(list_obj.value['main']['temp']))
                  feels_like.append(kelvinToFahrenheit(list_obj.value['main']['feels_like']))
                  temp_min.append(kelvinToFahrenheit(list_obj.value['main']['temp_min']))
                  temp_max.append(kelvinToFahrenheit(list_obj.value['main']['temp_max']))
                  pressure.append(list_obj.value['main']['pressure'])
                  sea_level.append(list_obj.value['main']['sea_level'])
                  grnd_level.append(list_obj.value['main']['grnd_level'])
                  humidity.append(list_obj.value['main']['humidity'])
                  temp_kf.append(list_obj.value['main']['temp_kf'])
    
              if('weather' in list_obj.value):
                  for weather1 in list_obj.value['weather']:
                      weather_forcast.append(weather1['main'])
                      weather_description.append(weather1['description'])
    
              if('visibility' in list_obj.value):
                  visibility.append(list_obj.value['visibility'])
              else:
                  visibility.append("")
    
    
              if('clouds' in list_obj.value):
                  clouds.append(list_obj.value['clouds'])
              else:
                  clouds.append("")
    
              if('wind' in list_obj.value):
                  wind.append(list_obj.value['wind'])
              else:
                  wind.append("")
        
              if('pop' in list_obj.value):
                  pop.append(list_obj.value['pop'])
              else:
                  pop.append("")
    
              if('rain' in list_obj.value):
                  rain.append(list_obj.value['rain'])
              else:
                  rain.append("")
        
          d = {'data': [{'date_fixed': str(a), 'temp': str(t), 'feels_like': str(fl), 'temp_min': str(tmin), 'temp_max': str(tmax), 'pressure': str(p), 'sea_level': str(sl), 'grnd_level': str(gl), 'humidity': str(h), 'temp_kf': str(tkf), 'weather_forcast': str(wf), 'weather_description': str(wd), 'clouds': str(c), 'wind': str(w), 'visibility': str(v), 'pop': str(pop), 'rain':str(r)} for a, t, fl, tmin, tmax, p, sl, gl, h, tkf, wf, wd, c, w, v, pop, r in zip(date_fixed, temp, feels_like, temp_min, temp_max, pressure, sea_level, grnd_level, humidity, temp_kf, weather_forcast, weather_description, clouds, wind, visibility, pop, rain)]}

          return d
        else:
          return {"Error": "Error Getting Weather Data" }
      else:
        return {"Error": "Error GeoCoding Zipcode" }
  else:
    return f'API Key Error'

if __name__ == "__main__":
  app.run(host='localhost', port=8000, debug=True)