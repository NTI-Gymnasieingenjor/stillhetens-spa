import glob
import subprocess
import os
import json
from colorama import Fore, Back, Style

def Loops(type):
    for i in list[type]:
        print(i)

def sendFileAndPrint(filePath: str):
    request = json.loads(os.popen('curl -s -H "Content-Type: multipart/form-data" -F "text=<' + filePath + ';type=text/plain" -F "output=json" https://jigsaw.w3.org/css-validator/validator').read())
    global list 
    list = request["cssvalidation"]
    if list["result"]["errorcount"] > 0:
        print(Back.RED + "ERROR" + Style.RESET_ALL)
        Loops("errors")

    if list["result"]["warningcount"] > 0:
        print(Back.YELLOW + Fore.BLACK + "WARNING" + Style.RESET_ALL)
        Loops("warnings")
    if list["result"]["warningcount"] == 0 and list["result"]["errorcount"] == 0:
        print(Back.GREEN + Fore.BLACK + "Validation succeded" + Style.RESET_ALL)
    
for file in glob.glob("../../public/assets/less/dist/*.css"):
    sendFileAndPrint(file)
