import cv2
from PIL import Image
import numpy as np
import sys
import os

source_path = "./work/source/"
source = os.listdir("./work/source")
dest_path = "./work/dest/"

for i in source:
    try:

        # 사진 크기 추출
        target = source_path + i
        img_origin = Image.open(target)
        img_w, img_h = img_origin.size

    except:
        
        print("missed: " + i)
        break

    else:

        # item 크기 추출 

        image = cv2.imread(target)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


        # 패딩 사이즈 정하기 
        x,y,item_w,item_h = cv2.boundingRect(thresh)
        padding = int(item_w * 0.2)

        downpercent = round((img_w - 2 * padding) / item_w, 2)

        if downpercent > 1:
            fname, _ = i.split(".")
            img_origin.save(dest_path + fname + ".png","PNG")
            break

        new_img_w = int(img_w * downpercent)
        new_img_h = int(img_h * downpercent)

        img = Image.open(target)

        final_img = img.resize((new_img_w, new_img_h))

        # 표시 용도 (지워도 됨)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        # cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

        # cv2.imshow("image", image)
        # cv2.waitKey()


        # background
        background = Image.open("./work/background.jpg")
        background = background.resize((img_w, img_h))

        background_w = (img_w - new_img_w) // 2
        background_h = (img_h - new_img_h) // 2

        background.paste(final_img, (background_w, background_h))
        #background.paste(img, (0, 0))

        fname, _ = i.split(".")

        background.save(dest_path + fname + ".png","PNG")

    finally:

        continue