import streamlit as st
from PIL import Image
import cv2
import numpy as np

# Set Streamlit layout
st.set_page_config(layout="wide")

st.markdown("<p style='font-size: 50px; color: orange; font-weight: bold;'>AI Photograph Analysis</p>", unsafe_allow_html=True)


image_path = "/Users/vjmanoj/Downloads/chatbot (1).png"

# Display the image using st.image
st.image(image_path)
st.write("Choose the photos you would like us to analyze")

uploaded_images = st.file_uploader("Upload one or more images (JPG or PNG)", type=["jpg", "png"], accept_multiple_files=True)

wanted_list = []
unwanted_list = []

# Analyze the image for blurriness
def blurry(image_input):
    img = np.array(image_input)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    var = cv2.Laplacian(grey, cv2.CV_64F).var()
    blur_index = var / 1.5
    return var < 120


if uploaded_images is not None:
    st.write("Your uploaded images: ")
    for i in uploaded_images:
        # Open the uploaded image using Pillow (PIL)
        image = Image.open(i).convert("RGB")  
        scale_factor = 0.5  # Adjust the scale factor as needed
        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)
        # Scale down the image
        scaled_image = image.resize((new_width, new_height))
        st.image(scaled_image)

        if blurry(scaled_image):
            unwanted_list.append(scaled_image)
        else:
            wanted_list.append(scaled_image)

st.markdown("<p style='font-weight: bold; color: green;'>GOOD IMAGES</p>", unsafe_allow_html=True)
for image in wanted_list:
    st.image(image)

st.write("")
st.write("")
st.write("")

st.markdown("<p style='font-weight: bold; color: red;'>BAD IMAGES</p>", unsafe_allow_html=True)
for image in unwanted_list:
    st.image(image)
