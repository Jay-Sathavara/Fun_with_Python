# JP0030

import tkinter as tk
from tkinter import *

window=Tk()#creating a window
window.title("PythonGeeks")#title of the window
window.geometry("500x500")#geometry of the window
#create a label
Label(window,text="WEIGHT CONVERTER",font=("Arial", 20 ),bg="black",fg='yellow').pack()

kg=tk.IntVar()#kg is integer type

def convert_to_gram():
