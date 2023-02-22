#!/usr/bin/python3
#打印分辨率300dpi,卡片59x86
#
import os
import math
from PIL import Image
inImg_w=697#小图片宽
inImg_h=1016#小图片高

a4_w=2479
a4_h=3508

rows=3#排列行数
cols=3#排列列数
inImg_fram=97#小图片的边框，单位是像素(2479-687*3)/4
inImg_path="./Yu-Gi-Oh-in" 


def merge():
  global inImg_w,inImg_h
  global rows
  global cols
  global inImg_fram
  print (inImg_fram)
  files=os.listdir(inImg_path)
  #files.sort(key=lambda x:int(x[4:-5]))
  out = Image.new('RGBA', (a4_w, a4_h))
  
  row = 0
  col = 0
  for file in files:
    print(file)
    image = Image.open(inImg_path+"/"+file)
    image_resize = image.resize((inImg_w, inImg_h), Image.ANTIALIAS)
    
    out.paste(image_resize, (col * (inImg_w+inImg_fram)+inImg_fram, row * (inImg_h+inImg_fram)+inImg_fram))
    col += 1
    if col == cols:
      row += 1
      col = 0

  out.save("out.png")

merge()