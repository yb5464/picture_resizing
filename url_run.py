import os
import urllib.request
from openpyxl import load_workbook
import numpy as np
from urllib.request import urlopen
import cv2
import os
current_path = os.getcwd()

try: 
    os.mkdir(current_path + "/work/source")
except:
    pass


def readimg(self, img_url):
    from urllib.request import urlopen, Request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=img_url, headers=headers) 
    with urlopen(req) as response:
        return response.read()





num_list = []
url_list = []

source_path = "./work/source/"
source = os.listdir("./work/source")
dest_path = "./work/dest/"

load_wb = load_workbook("./ounce.xlsx", data_only = True)

load_ws = load_wb["최종"]

for row in load_ws.rows:
    num_list.append(row[0].value)
    url_list.append(row[3].value)
    #url_list.append("http:" + str(row[3].value.split(":")[1]))

for url in url_list:
    (url)



# for index in range(len(num_list)):
#     try:
#         urllib.request.urlretrieve(url_list[index], source_path + str(num_list[index]) + ".jpg")
#     except:
#         print("missed: ", index)
#         continue