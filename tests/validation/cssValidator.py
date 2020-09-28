import glob
import os
import json
from colorama import Fore, Back, Style

# The variable that turns to true when there's an error
global exitVar
exitVar = False


def printMessage(type: str, filePath: str):
    # For-loop that prints out all the errors and warnings in the "output" list
    for i in output[type]:
        print("---------------------------------------------------------------------")
        if type == "errors":
            print(Back.RED + "ERROR" + Style.RESET_ALL)
        elif type == "warnings":
            print(Back.YELLOW + Fore.BLACK + "WARNING" + Style.RESET_ALL)
        print("Fil:", filePath.replace("../../", ""))
        print("Radnummer:", i["line"])
        print("Meddelande:", i)


def sendFileAndPrint(filePath: str):
    # Sets the variable output as a global variable
    # It runs the curl command in terminal and then converts the resulting json to a python dictionary
    global output
    output = json.loads(os.popen('curl -s -H "Content-Type: multipart/form-data" -F "text=<' + filePath +
                                 ';type=text/plain" -F "output=json" https://jigsaw.w3.org/css-validator/validator').read())["cssvalidation"]

    # Creates the count variables
    errorCount = output["result"]["errorcount"]
    warningCount = output["result"]["warningcount"]

    # When there are errors, prints them out
    if errorCount > 0:
        global exitVar
        exitVar = True
        printMessage("errors", filePath)
    # When there are warnings, prints them out
    if warningCount > 0:
        printMessage("warnings", filePath)

    # When there aren't any errors or warnings
    if errorCount == 0 and warningCount == 0:
        print(Back.GREEN + Fore.BLACK + "CSS Validation succeeded" + Style.RESET_ALL)

    print("---------------------------------------------------------------------")

# Looks for all the CSS files in the public/assets/less/dist directory to send to the validator
for file in glob.glob("../../public/assets/less/dist/*.css"):
    sendFileAndPrint(file)

# If error message occurs, validation fails
if exitVar == True:
    print(Back.RED + "CSS Validation Failed" + Style.RESET_ALL)
    exit(1)
