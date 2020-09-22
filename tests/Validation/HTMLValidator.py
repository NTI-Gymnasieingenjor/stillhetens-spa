import requests
import json
import glob
from colorama import Fore, Back, Style

def sendFileAndPrint(filePath: str):
    htmlFile = open(filePath, 'rb').read()
    headers = {'Content-Type': 'text/html'}
    req = requests.post(url='http://validator.w3.org/nu/?out=json', data=htmlFile, headers=headers)
    output = req.json()["messages"]
    if len(output) == 0:
        print("Validation Succeded")
        pass
    else:
        exitVar = False
        for i in range(len(output)):
            exitVar = True
            messages = output[i]
            print("--------------------")
            if messages["type"] == "error":
                print(Back.RED + "ERROR" + Style.RESET_ALL)
            if messages["type"] == "info":
                print(Back.YELLOW + Fore.BLACK + "WARNING" + Style.RESET_ALL)
            print("Fil:", filePath)
            print("Radnummer:",messages["lastLine"])
            print("Meddelande:", messages["message"])
            print("--------------------")
        if exitVar == True:
            exit(1)
for file in glob.glob("../../public/*.html"):
    sendFileAndPrint(file)