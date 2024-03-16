class Prompt:
    def get_prompt(self):
        prompt_text="""
        you are nutrionist expert.
        I will provide you image of a packaged food wrapper,then I will ask you to provide me information which is there in the image.
        Image contains tablular data for nutrition and ingredients.Extract exact below nutritional information from image. 
        (Energy Value,Protein,Carbohydrate,Total Sugars,Added Sugars,Total Fat,Saturated Fat,Trans Fat,Cholestrol,Sodium,Dietry Fibre) and give output for  per 100 g serving in Json Format.
        If Some information is not provided on wrapper then return Json having null value for particular nutrition.
        """
        return prompt_text