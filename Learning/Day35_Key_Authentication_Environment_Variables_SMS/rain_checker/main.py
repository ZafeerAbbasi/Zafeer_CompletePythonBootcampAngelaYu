import requests

api_key = "d6cefb3a0bdda8392b60101d7ad27a73"
params = {
    "appid": "d6cefb3a0bdda8392b60101d7ad27a73",
    "lat": 49.137051,
    "lon": -122.841766,
    "units": "metric",
    "cnt": 4
}

response = requests.get( url="https://api.openweathermap.org/data/2.5/forecast", params=params )
response.raise_for_status( )

weather_data = response.json( )

will_rain = False

for entry in weather_data["list"]:
    weather_code = entry["weather"][ 0 ]["id"]
    if( int( weather_code ) < 700 ):
        will_rain = True

if will_rain:
    print( "bring an umbrella" )


