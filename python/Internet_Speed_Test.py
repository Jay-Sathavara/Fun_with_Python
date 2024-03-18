# JP0030

from tkinter import *
from speedtest import Speedtest

# Creation OF Function
def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps")