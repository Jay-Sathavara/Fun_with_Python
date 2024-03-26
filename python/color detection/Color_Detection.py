# JP0030

# Color_detection.py – main source code of our project.
# Kedaar_Nath.jpg – sample image for experimenting.
# Colors.csv – a file that contains our dataset.

import cv2
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

