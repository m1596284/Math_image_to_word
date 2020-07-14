import os
pyPath, filename = os.path.split(__file__)
# 分析圖片轉換成文字 英文 中文 數字
import pytesseract
import PIL.Image
import PIL.ImageDraw
from PIL import *
from PIL import ImageEnhance
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#影像前處理 (二分化)
def binarizing(img,threshold): #input: gray image
     pixdata = img.load()
     w, h = img.size
     for y in range(h):
       for x in range(w):
           if pixdata[x, y] < threshold:
               pixdata[x, y] = 0
           else:
               pixdata[x, y] = 255
     return img

# 範例test.png 地址
left = 1200
right = 2194
top = 690
bottom = 737
img = Image.open(pyPath + "/P.png").convert("L")
# img = Image.open(pyPath + "/P.png")

# img = img.crop((left,top,right,bottom))
# binarizing(img,210)
# img.show()
logAdd = pytesseract.image_to_string(img, lang='chi_sim')
f = open(pyPath + "/P_test.txt","w", encoding='UTF-8') 
f.write(logAdd)
f.close
print(logAdd)