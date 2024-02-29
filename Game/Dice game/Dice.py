# JP0030

import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Data Flair Roll the Dice')

l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="Hello from Data Flair!", fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()

dice = ['side1.png', 'side2.png', 'side3.png', 'side4.png', 'side5.png', 'side6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1

label1.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label1.configure(image=image1)
    
    label1.image = image1

button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

button.pack( expand=True)

root.mainloop()
