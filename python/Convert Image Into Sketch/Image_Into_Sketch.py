# JP0030

import cv2 as cv

image = cv.imread("iron.jpeg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

invert_image = cv.bitwise_not(gray_image)

