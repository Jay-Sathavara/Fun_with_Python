# JP0030

import tkinter as tk
import random
from functools import partial

window = tk.Tk()
window.geometry("500x500")
window.title(' JP0030 - Clickomania game')

Nav = tk.Frame(master=window, pady=5, padx=16)
Main = tk.Frame(master=window, pady=16, padx=16)
Footer = tk.Frame(master=window, pady=16, padx=16)
Nav.pack(expand=True)
Main.pack(expand=True)
Footer.pack(expand=True)