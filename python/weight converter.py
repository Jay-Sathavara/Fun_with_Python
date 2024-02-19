# JP0030

import tkinter as tk
from tkinter import *

window=Tk()
window.title("PythonGeeks")
window.geometry("500x500")

Label(window,text="WEIGHT CONVERTER",font=("Arial", 20 ),bg="black",fg='yellow').pack()

kg=tk.IntVar()

def convert_to_gram():
    kg1=kg.get() 
    gram = float(kg1)*1000 
    Label(window,text="This weight in grams would be",font=("Arial", 12 )).pack()
    Label(window,text=gram,bg="red").pack()

