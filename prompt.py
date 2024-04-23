class Prompt:
    def foodlabel_prompt(self):
        prompt_text="""
        you are an optical character recognition expert.
        I will provide you an image of a packaged food wrapper,then I will ask you to provide me information which is there in the image.
        Which food item does the wrapper represents?
        What is the net quantity/weight present in the wrapper of food item?
        """
        return prompt_text
    
    def nutritioninfo_prompt(self):
        prompt_text="""
        you are nutrionist expert.
        I will provide you image of a packaged food wrapper,then I will ask you to provide me information which is there in the image.
        Image contains tablular data for nutrition and ingredients.Extract exact below nutritional information from image. 
        (Energy Value,Protein,Carbohydrate,Total Sugars,Added Sugars,Total Fat,Saturated Fat,Trans Fat,Cholestrol,Sodium,Dietry Fibre) and give output for  per 100 g serving in Json Format.
        If Some information is not provided on wrapper then return Json having null value for particular nutrition.
        """

        return prompt_text
    
    def rating_prompt(self):
        prompt_text="""
        you are a nutrition and health expert.
        I will provide you an image of a packaged food wrapper.
        Analyse nutritional information and ingredients present on wrapper and based on your knowledge in health and nutrition rate the food item on a scale of 1-5.Give 1 rating if item has negative health impact and give 5 rating if item has positive health impact.
        """
        return prompt_text