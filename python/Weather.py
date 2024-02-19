# JP0030

import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

def getNotification():
    cityName=place.get() 
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" 
    try:

        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(complete_url) 
        x = response.json() 
        y = x["main"] 
 
        temp = y["temp"]

        pres = y["pressure"]

        hum = y["humidity"]

        z = x["weather"]

        weather_desc = z[0]["description"]

        info="Here is the eather description of "+ cityName+ ":"+" \nTemperature = " +str(temp) +"°C"+"\n atmospheric pressure = " + str(pres) + "hPa"+"\n humidity = " +str(hum) +"%"+"\n description of the weather= " + str(weather_desc)

      
