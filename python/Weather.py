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
 
     