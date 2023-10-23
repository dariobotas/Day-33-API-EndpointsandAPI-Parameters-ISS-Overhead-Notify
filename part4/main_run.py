import requests as api


def main():
  response = api.get(url='http://api.open-notify.org/iss-now.json')
  print(f"Status: {response.status_code}")
  #Actual json response
  print(response.json())
  print(response.json()['iss_position']["longitude"])
  print(response.json()['iss_position']["latitude"])
 
  
  response = api.get(url='http://api.open-notify.org/is-now.json')
  print(f"Status: {response.status_code}")

  #Not a good way to code responses - not very specific description
  #if response.status_code != 200:
   # raise Exception("Bad response from ISS API")

  #Better way (?)
  #if response.status_code == 404:
   #raise Exception("That resource does not exist.")
  #elif response.status_code == 401:
   #raise Exception("You are not authorized to access that resource.")

  #Easiest one
  response.raise_for_status()
"""
API Status Responses
1XX: Hold On
2XX: Here you go
3XX: Go Away
4XX: You Crewed Up
5XX: I Screwed Up
"""
