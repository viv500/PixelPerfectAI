import cv2
import PIL 
from PIL import Image
import numpy as np

image_input=input("Enter the file directory: ")
print()

def blurry():
    # Read the image
    img = cv2.imread(image_input)

    # Convert to greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the laplacian of this image and
    # calculate the variance
    var = cv2.Laplacian(grey, cv2.CV_64F).var()

    # if variance is less than the set threshold
    # image is blurred otherwise not
    blur-index=var/1.5
    if var < 120:
        print('Sharpness: Image is Blurry. \n Sharp index: ',blur-index)
    else:
        print('Sharpness: Image is Sharp \n Sharp index:',blur-index)
