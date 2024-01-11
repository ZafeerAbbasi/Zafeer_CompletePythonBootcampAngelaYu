import requests
from tkinter import *
import datetime as dt

# reponse = requests.get( url="http://api.open-notify.org/iss-now.json" )
# reponse.raise_for_status( )

# data = reponse.json( )
# print( data )

parameters = {
    "lat": 49.137050,
    "lng": -122.841770,
    "tzid":"Canada/Pacific ",
    "formatted":0
}

response = requests.get( url="https://api.sunrise-sunset.org/json" , params=parameters )
response.raise_for_status( )
sunrise_time = response.json( )["results"]["sunrise"].split( "T" )[1].split( "+" )[0]
current_time = dt.datetime.now( ).__str__( ).split( " " )[ 1 ][:8]

print( sunrise_time ) 
print(  current_time )