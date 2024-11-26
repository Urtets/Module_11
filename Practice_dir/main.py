from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pprint
from bs4 import BeautifulSoup
import html5lib

def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))

im = new_photo("pancake-with-caviar-tea.jpg")

top_im = Image.open('crazy_emogi.png')
pprint.pprint(dir(Image))

width, height = im.size
offset = (width // 2, height // 2)
im.paste(top_im, offset)


draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 50)
draw.text((0, 10), "Вкусные вкусности", font=font, fill='rgb(230, 255, 150)')

im.show()

# im.show()

# print(dir(Image))









# with open("F:/Программирование/MyApp/Front/RegistrationForm/Registration.html", 'rb') as func_:
#     document = func_.read()
#
# soup = BeautifulSoup(document, 'lxml')
#
# print(soup.body)