# JP0030

from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk
import moviepy.editor as mp

class VideoAudioConverter:

    def __init__(self, root):
        self.root = root
        self.root.title("VIDEO-AUDIO CONVERTER by DataFlair")
        self.root.geometry('1280x720')
        self.bg = ImageTk.PhotoImage(file="bg_image.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0)

        Button(self.root,text="Browse Files",font=("times new roman", 15),command=self.browse).place(x=40, y=630)

    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Select a File", filetypes=(("Video files", "*.mp4*"),))

        Label(self.root, text=os.path.basename(self.file_name), font=("times new roman", 20), bg="blue").place(x=200, y=630)

        Label(self.root, text='Processing...', font=("times new roman", 30)).place(x=600, y=630)
        self.convert(os.path.basename(self.file_name))

        Label(self.root, text='Completed!!', font=("times new roman", 30)).place(x=1000, y=630)
