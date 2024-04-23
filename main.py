# Streamlit application for uploading file and fetching nutritional information
import streamlit  as st 
import numpy as np
import cv2
import os
import json
from PIL import Image

from user import User

st.write("Get Nutritional Information")

uploaded_file = st.file_uploader('Upload an image for which you want nutritional information', type=['txt','png','jpg'])

# Get image uploaded by User and display it
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Save the uploaded image 
    img_path='Uploaded_Images/temp_img.jpg'
    cv2.imwrite(img_path,opencv_image)

    # Get Nutritional information from the uploaded image
    user1=User('u1')
    user1.upload_image(img_path)
    # Get wrapper label
    wrapper_label=user1.get_foodlabel()
    st.write(f" :green[Uploaded image corresponds to food item:]")
    st.write(wrapper_label)

    # Get wrapper nutrition information
    wrapper_nutrition=user1.get_nutrition_info()
    wrapper_nutrition_json=json.loads(wrapper_nutrition)
  
    st.write(f" :green[Uploaded image and corresponding Nutritional Information per 100 g serving is as follows:]")
    col1,col2=st.columns(2)
    with col1:
        st.image(opencv_image,width=300,channels="BGR")
    with col2:
        st.json(wrapper_nutrition_json)

    # Get Rating of food item
    wrapper_rating=user1.get_foodrating()
    st.write(f" :green[Rating of food item on a scale of 1-5 is:]")
    st.write(wrapper_rating)












