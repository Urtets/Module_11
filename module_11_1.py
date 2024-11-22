"""
open weather app using requests
"""
"""
import requests

api_weather_key = 'f5d6edc003514f46ca744aba91ebc106'
api_weather_url = 'http://api.openweathermap.org/data/2.5/find'


params = {'q': "Krasnodar,RU", 'appid': api_weather_key}
try:

    response = requests.get(api_weather_url, params=params)

    data = response.json()
    some_info = ["{} ({})".format(d['name'], d['sys']['country'])
                 for d in data['list']]
    print(some_info)
    city_id = data['list'][1]['id']
    print(city_id)

except Exception as e:
    print(e)
    # pass

city_id = '542420'
api_weather_url_2 = 'http://api.openweathermap.org/data/2.5/weather'
params_2 = {'id': city_id, 'units': 'metric', 'APPID': api_weather_key}

try:
    response_2 = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params_2)
    data_2 = response_2.json()
    print(data_2)
    print("Krasnodar", data_2['main']['temp'], "degrees Celsius")
except Exception as e:
    print(e)
"""

"""
using pandas
"""

import pandas
import numpy

series = pandas.Series([1, 2, 3, 'scddsc'])
print(series)

dates = pandas.date_range('20240101', periods=8)
print(dates)

data_frame = pandas.DataFrame(numpy.random.randint(1, 10), index=dates, columns=list("ABCD"))
print(data_frame)