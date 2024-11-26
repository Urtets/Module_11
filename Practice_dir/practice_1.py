from PIL import Image
from PIL import ImageFont, ImageDraw, ImageColor
import numpy as np


class PostMaker:
    def __init__(self, photo_name):
        self.image = Image.open(photo_name)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2,))

    def paste(self, photo_name):
        paste_image = Image.open(photo_name, 'r')

        paste_image = paste_image.resize((paste_image.size[0] // 8, paste_image.size[1] // 8))

        paste_image = paste_image.convert('L')

        self.image.paste(paste_image, (0, 170), mask=paste_image)

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("Gemina2laserital.ttf", 60)
        draw.text((50, -10), text, font=font, fill='rgb(115, 113, 113)')
        self.image.show()

    def find_pic_colors(self, some_pic: Image):
        width = some_pic.size[0]
        height = some_pic.size[1]
        for i in range(0, width):
            for j in range(0, height):
                data = some_pic.getpixel((i, j))
                print(data)




if __name__ == "__main__":
    image = PostMaker('animated_casper.jpeg')
    image.paste('Casper_English_logo.png')
    image.upgrade("Hi, There!")
