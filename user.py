from model import *
from wrapper_image import *
from prompt import *

class User:
    def __init__(self,user_id):
        self.user_id=user_id
        self.model_obj=Model('gemini-pro-vision')
        self.prompt_obj=Prompt()

    def upload_image(self,image_path):
        self.image_path=image_path
        image_obj=WrapperImage(self.image_path)
        self.image=image_obj.load_image()

    def get_nutrition_info(self):
        prompt_text=self.prompt_obj.nutritioninfo_prompt()
        output=self.model_obj.get_model_output(prompt_text,self.image)
        # pre-processing string output
        output=output.replace('json','')
        output=output.replace("```",'')
           
        return output
    
    def get_foodlabel(self):
        prompt_text=self.prompt_obj.foodlabel_prompt()
        output=self.model_obj.get_model_output(prompt_text,self.image)
           
        return output
    
    def get_foodrating(self):
        prompt_text=self.prompt_obj.rating_prompt()
        output=self.model_obj.get_model_output(prompt_text,self.image)

        return output