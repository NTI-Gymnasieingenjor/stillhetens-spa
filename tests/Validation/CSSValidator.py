import glob
import subprocess
import os
import json

def sendFileAndPrint(filePath: str):
    request = os.popen('curl -s -H "Content-Type: multipart/form-data" -F "text=<' + filePath + ';type=text/plain" -F "output=json" https://jigsaw.w3.org/css-validator/validator').read()
    json_string = request
    obj = json.loads(json_string)
    print(obj["cssvalidation"])


for file in glob.glob("../../public/assets/less/dist/*.css"):
    sendFileAndPrint(file)
