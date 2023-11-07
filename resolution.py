import cv2
import PIL 
from PIL import Image
import numpy as np

def img_resolution():
    # loading the image
    img = PIL.Image.open(image_input)

    # fetching the dimensions
    wid, hgt = img.size

    # displaying the dimensions
    print("Image Resolution: ",(str(wid) + "x" + str(hgt)))
