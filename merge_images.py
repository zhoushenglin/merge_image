#!/usr/bin/python3
import os
import math
from PIL import Image
inImg_w=580#小图片宽
inImg_h=640#小图片高
rows=8#排列行数
cols=6#排列列数
inImg_fram=20#小图片的边框，单位是像素
inImg_path="./in" 


def merge():
  global inImg_w,inImg_h
  global rows
  global cols
  global inImg_fram
  print (inImg_fram)
  files=os.listdir(inImg_path)
  files.sort(key=lambda x:int(x[4:-5]))
  out = Image.new('RGBA', (cols*(inImg_w+inImg_fram*2), rows*(inImg_h+inImg_fram*2)))
  
  row = 0
  col = 0
  for file in files:
    print(file)
    image = Image.open(inImg_path+"/"+file)
    out.paste(image, (col * (inImg_w+inImg_fram), row * (inImg_h+inImg_fram)))
    col += 1
    if col == cols:
      row += 1
      col = 0

  out.save("out.png")

merge()