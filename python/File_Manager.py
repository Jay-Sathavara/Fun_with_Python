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
