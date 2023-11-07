import cv2
import PIL 
from PIL import Image
import numpy as np

def assess_lighting(image_path):
    try:
        # Read the image
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate the mean and standard deviation of pixel intensities
        mean_intensity = np.mean(gray_image)
        std_intensity = np.std(gray_image)

        # Define a threshold for assessing lighting conditions (you can adjust this threshold)
        threshold = 50  # Adjust as needed

        if std_intensity < threshold:
            print("The image appears to have low lighting.\n Light Rating: ",std_intensity)
        else:
            print("The image appears to have adequate lighting. \n Light Rating: ",std_intensity)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = input("Enter the file path to the image: ")
    assess_lighting(image_path)
