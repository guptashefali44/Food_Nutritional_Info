from model import *
from wrapper_image import *
from prompt import *

class User:
    def __init__(self,user_id):
        self.user_id=user_id
    def upload_image(self,image_path):
        self.image_path=image_path
    def get_nutrition_info(self):
        prompt_obj=Prompt()
        prompt_text=prompt_obj.get_prompt()

        image_obj=WrapperImage(self.image_path)
        image=image_obj.load_image()

        model_obj=Model('gemini-pro-vision')
        output=model_obj.get_model_output(prompt_text,image)

        return output