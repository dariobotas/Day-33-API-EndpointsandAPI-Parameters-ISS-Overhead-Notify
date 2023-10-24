import requests as api
import datetime as dt

MY_LAT = 51.587351
MY_LNG = -0.127758

"""response = api.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

lon = data['iss_position']['longitude']
lat = data['iss_position']['latitude']

iss_posi = (lon,lat)

print(iss_pos)"""

parameters = {
  "lat": MY_LAT,
  "lng": MY_LNG,
  "formatted": 0
}

response = api.get(url='http://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
print(data["results"]["sunrise"])
print(data["results"]["sunset"])



time_now = dt.datetime.now()
print(time_now)

"""
API Status Responses
1XX: Hold On
2XX: Here you go
3XX: Go Away
4XX: You Crewed Up
5XX: I Screwed Up
"""
