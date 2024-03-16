from PIL import Image

class WrapperImage:
    def __init__(self,image_loc):
        self.image_loc=image_loc

    def load_image(self):
        image=Image.open(self.image_loc)
        return image