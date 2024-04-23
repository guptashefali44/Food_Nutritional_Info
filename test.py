import streamlit  as st 
import numpy as np
import cv2
import os
from PIL import Image
import json
from user import User


#st.write("Get Nutritional Information")

# uploaded_file = st.file_uploader('Upload an image for which you want nutritional information', type=['txt','png','jpg'])
# # save uploaded image on path Uploaded_Images
# print(type(uploaded_file))

user1=User('u1')
user1.upload_image('WrapperPhotos/IMG_3931.jpg')
model_output=user1.get_nutrition_info()
model_output.strip('json')
print(type(model_output))
print(model_output)

model_output_json=json.loads(model_output)
print(type(model_output_json))
print(model_output_json)