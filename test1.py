# -- coding: UTF-8 --
import pytesseract
from PIL import Image

text1 = pytesseract.image_to_string(Image.open('text1.JPG'),lang='chi_sim')
print(text1)