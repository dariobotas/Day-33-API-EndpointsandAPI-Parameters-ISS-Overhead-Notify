import requests as api


def main():
    response = api.get(url='http://api.open-notify.org/iss-now.json')
    print(f"Status: {response.status_code}")

    response = api.get(url='http://api.open-notify.org/is-now.json')
    print(f"Status: {response.status_code}")


"""
API Status Responses
1XX: Hold On
2XX: Here you go
3XX: Go Away
4XX: You Crewed Up
5XX: I Screwed Up
"""
