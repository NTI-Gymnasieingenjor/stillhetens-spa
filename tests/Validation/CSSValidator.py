import glob
import os


def sendFileAndPrint(filePath: str):    
    request = os.system('curl -s -H "Content-Type: multipart/form-data" -F "text=<' + filePath + ';type=text/plain" -F "output=json" https://jigsaw.w3.org/css-validator/validator')
    print(request)


for file in glob.glob("../../public/assets/less/dist/*.css"):
    sendFileAndPrint(file)