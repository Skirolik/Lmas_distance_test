import requests


def get_weather_data(lat, lon):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': "350ce365561bfae47cbfc3ca2f5f59d3"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        id=data['weather'][0]['description']
        #print('id',id)

        return id
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")
        return None