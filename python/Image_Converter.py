# JP0030

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from pdf2image import convert_from_path

root = Tk()
root.geometry('600x250')
root.title('JP0030')
Label(root,text='Image Format Converter',font='arial 15').place(x=210,y=10)

def browse():
    global img
    filename = filedialog.askopenfilename(title = "Select a File")
    img = Image.open(filename)

Button(root,text='Browse an Image',command=browse,fg='blue',font='arial 10').place(x=250,y=45)


def png_to_jpg():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)

def jpg_to_png():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    img.save(export_file_path)

Button(root,text='Png To Jpg',command=png_to_jpg,fg='red',font='arial 10').place(x=120,y=95)
Button(root,text='Jpg To Png',command=jpg_to_png,fg='red',font='arial 10').place(x=450,y=95)

root.mainloop()