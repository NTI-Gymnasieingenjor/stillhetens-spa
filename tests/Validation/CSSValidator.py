import requests
import glob
import os
import urllib3
from poster3.encode import multipart_encode
import base64


def sendFileAndPrint(filePath: str):    
    request = os.system('curl -s -H "Content-Type: multipart/form-data" -F "text=<' + filePath + ';type=text/plain" -F "output=json" https://jigsaw.w3.org/css-validator/validator')
    print(request)


for file in glob.glob("./*.css"):
    sendFileAndPrint(file)