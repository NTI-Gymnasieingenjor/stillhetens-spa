import requests
import json
import glob
from colorama import Fore, Back, Style

# The variable that turns to true when there's an error
global exitVar
exitVar = False


def sendFileAndPrint(filePath: str):
    # Creates a variable that opens the HTML file and stores the data in binary format
    htmlFile = open(filePath, 'rb').read()
    # Specifies to the validator that the content that is being sent to it is a HTML file
    headers = {'Content-Type': 'text/html'}
    # Sends a request to the validator that includes the content in the HTML file
    req = requests.post(
        url='http://validator.w3.org/nu/?out=json', data=htmlFile, headers=headers)
    # Variable that stores the output that is sent back from the validator
    # "messages" is a list that stores all the errors and warnings sent back from the validator
    output = req.json()["messages"]
    # If the "messages" list is empty, the validation succeeds
    if len(output) == 0:
        print(Back.GREEN + Fore.BLACK + "HTML Validation succeeded" + Style.RESET_ALL)
        pass
    else:
        # For-loop that prints out all the errors and warnings in the "messages" list
        for i in range(len(output)):
            global exitVar
            exitVar = True
            messages = output[i]
            print("--------------------")
            # Color scheme for error messages
            if messages["type"] == "error":
                print(Back.RED + "ERROR" + Style.RESET_ALL)
            # Color scheme for warning messages
            if messages["type"] == "info":
                print(Back.YELLOW + Fore.BLACK + "WARNING" + Style.RESET_ALL)
            print("Fil:", filePath.replace("../../", ""))
            print("Radnummer:", messages["lastLine"])
            print("Meddelande:", messages["message"])
    print("---------------------------------------------------------------------")


# Looks for all the HTML files in the public directory to send to the validator
for file in glob.glob("../../public/*.html"):
    sendFileAndPrint(file)

# If error or warning message occurs, validation fails
if exitVar == True:
    print(Back.RED + "HTML Validation Failed" + Style.RESET_ALL)
    exit(1)
