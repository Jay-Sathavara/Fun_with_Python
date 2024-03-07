# JP0030

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
import shutil

def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])

    os.startfile(os.path.abspath(file))


def copy_file():
    file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
    except:
        mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')

def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])

    os.remove(os.path.abspath(file))

    mb.showinfo(title='File deleted', message='Your desired file has been deleted')


def rename_file():
    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])

    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file to")
    rename_wn.geometry("250x70"); rename_wn.resizable(0, 0)

    Label(rename_wn, text='What should be the new name of the file?', font=("Times New Roman", 10)).place(x=0, y=0)

    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=0, y=30)

    new_file_name = os.path.join(os.path.dirname(file), new_name.get()+os.path.splitext(file)[1])

    os.rename(file, new_file_name)
    mb.showinfo(title="File Renamed", message='Your desired file has been renamed')


def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)