# JP0030

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from pdf2image import convert_from_path

root = Tk()
root.geometry('600x250')
root.title('DataFlair')
Label(root,text='Image Format Converter',font='arial 15').place(x=210,y=10)

def browse():
    global img
    filename = filedialog.askopenfilename(title = "Select a File")
    img = Image.open(filename)

Button(root,text='Browse an Image',command=browse,fg='blue',font='arial 10').place(x=250,y=45)

