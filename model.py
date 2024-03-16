import google.generativeai as genai

class Model:
    def __init__(self,model_name):
        self.model_name=model_name   

    def get_model_output(self,input,image):
        if self.model_name=='gemini-pro-vision':
            genai.configure(api_key='AIzaSyC-9oFWTojImSmk8tS3xjs3DM1RyBc7nyQ')
            model = genai.GenerativeModel(self.model_name)
            if input!="":
                response = model.generate_content([input,image])
            else:
                response = model.generate_content(image)
        return response.text