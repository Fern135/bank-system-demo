import random
import datetime
import string
from this import d
import colorama
import json
import platform
import os
#region validating email
import re
import string
# from validate_email_address import validate_email
#endregion
# import time
from os import system,name
from colorama import Fore
# from os.path import exists

colorama.init(autoreset=True) # colorful terminal


# for the coloring the console for debugging
success = Fore.GREEN
warning = Fore.YELLOW
error   = Fore.RED


GEN_API_KEY_CHOOSE = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

COMMANDS = {
    "pip-linux"          : "python3 -m pip install --upgrade pip",
    "pip-windows"        : "python -m pip install --upgrade pip",
    "update-package"     : "pip-review --auto", #<=======================> this is an external package for updating the packages
    "Decrypt-package"    : "pip-Decrypt", #<=============================> this is an external package for Decrypting what needs to be updated
    "windows-cls"        : "cls",
    "linux-cls"          : "clear",
    "install-pkg-win"    : "pip install -r requirements.txt",
    "install-pkg-linux"  : "pip3 install -r requirements.txt"
}


OS_SUPPORTED = {
    "mac"     : "Darwin",
    "linux"   : "Linux",
    "windows" : "Windows"
}


#region getting basic time, date, month, by day, weekday
def get_time() -> str:  # * get full 12 hour time
    return f'{datetime.datetime.now().strftime("%I")} : {datetime.datetime.now().strftime("%M")} {datetime.datetime.now().strftime("%p")}'


def get_Date() -> str:  # * get full date
    return datetime.datetime.now().strftime("%x")


def getMonth() -> str: # * full name of month
    return datetime.datetime.now().strftime("%B")


def getMonthDay() -> str: # * get the day of the month
    return datetime.datetime.now().strftime("%d")


def getWeekDay() -> str: # * get fullname of the weekday
    return datetime.datetime.now().strftime("%A")

#endregion


#region basic utilities
def generateAPIKey(Size) -> str:  # * generating the random api key and saving it with each user
    return ''.join(random.choice(GEN_API_KEY_CHOOSE) for _ in range(Size))


def pathJoinToCwd(current_path): # used for writeJson, writeToFile, and openJson
    os.path.join(os.getcwd(), current_path)

def openJson(title:str, json_usage='r') -> dict: # * opening json file
    with open(pathJoinToCwd(f"{title}.json"), json_usage) as f:
        return json.load(f.read())


def writeJson(path:str, title:str, data=None, writeType='w', indents=4) -> None:
    if data is None:
        data = {}
        
    # w for write. a whole new file,
    # a for appending to the end of the file
    with open(pathJoinToCwd(f"{path}/{title}.json"), writeType) as f:
        json.dump(data, f, indent=indents)


def writeToFile(path:str, title:str, file_type:str, data:str, writeType="w") -> None: # write to {path} with {title} holding {data} payload withe the {w} write type
    if path is None and title is None and data is None:
        return False

    f = open(pathJoinToCwd(f"{path}/{title}.{file_type}"), writeType)
    f.write(data)
    f.close()


def rnd(max:int) -> int:  # * random number generator default min = 1
    return random.randint(1, max)


def rnd(min:int, max:int) -> int:  # * random number generator between min and max
    return random.randint(min, max)


def evenRnd(min:int, max:int, step=2) -> int: # generating random even numbers
    return random.randint(min, max, step)


def oddRnd(min:int, max:int, step=3) -> int: # generating random odd numbers
    return random.randint(min, max, step)


def isDict(data) -> bool: # returns true or false if data is of type dict or not
    if type(data) is dict:
        return True
    else:
        return False

    
def isString(data) -> bool: # returns true or false if data is of type string or not
    if type(data) is str:
        return True
    else:
        return False

    
def isInt(data) -> bool: # returns true or false if data is of type int or not
    if type(data) is int:
        return True
    else:
        return False

    
def isFloat(data) -> bool: # returns true or false if data is of type float or not
    if type(data) is float:
        return True
    else:
        return False

    
def toInt(data) -> int: # type casting data to int
    return int(data)


def toFloat(data) -> float: # type casting data to Float
    return float(data)


def toString(data) -> str: # type casting data to String
    return str(data)


def toJson(data:dict): # dump data into a json object
    return json.dump(data)


def toUpper(data:str) -> str: # returns data as upper case
    return data.upper()


def toLower(data:str) -> str: # returns data as lower case
    return data.lower()


def isLower(data:str) -> bool: # returns true or false if data is lower case or not
    return data.islower()


def isUpper(data:str) -> bool: # returns true or false if data is lower case or not
    return data.islower()


def cls() -> None:  # * clear the console
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#endregion


#region advanced utilities
def getPcDevOs() -> str: # getting the os that the python script is runTerminalCommand on 
    return platform.system()


def delFile(title:str) -> None: # deleting specific file with title
    if os.path.exists(title):
      os.remove(title)
    else:
        return ("The file does not exist")


def runTerminalCommand(command) -> None: # runTerminalCommand terminal commands
    os.system(command)


def update_packages() -> None: # auto updater to be used in development
    try:
        if getPcDevOs() == OS_SUPPORTED['linux'] or getPcDevOs() == OS_SUPPORTED['mac']:
            # runTerminalCommand(COMMANDS["pip-linux"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            runTerminalCommand(COMMANDS["update-package"]) # update any packages that need updating
            runTerminalCommand(COMMANDS["install-pkg-linux"]) # install packages from requirements.txt

        elif getPcDevOs() == OS_SUPPORTED['windows']:
            # runTerminalCommand(COMMANDS["pip-windows"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            runTerminalCommand(COMMANDS["update-package"]) # update any packages that need updating
            runTerminalCommand(COMMANDS["install-pkg-win"]) # install packages from requirements.txt

        else:
            print(f" * {error}Unables to get os")
        
    except Exception as e:
        print(f" * {error}Error: {str(e)}")


def file_handler_v2(command): # handle files via commands. may or may not work
    """
        >>> file_handler_v2('remove --ask file1.txt file2.jpg file3.pdf')
        Please confirm: Removing files: ['file1.txt', 'file2.jpg', 'file3.pdf']
        
        >>> file_handler_v2('delete file1.txt file2.jpg file3.pdf')
        Removing files: ['file1.txt', 'file2.jpg', 'file3.pdf']

        !DO NOT USE
    """
    match command.split():
        case ['show']:
            print('List all files and directories: ')
            # code to list files

        case ['remove' | 'delete', *files] if '--ask' in files:
            del_files = [f for f in files if len(f.split('.'))>1]
            print('Please confirm: Removing files: {}'.format(del_files))
            # code to accept user input, then remove files

        case ['remove' | 'delete', *files]:
            print('Removing files: {}'.format(files))
            # code to remove files

        case _:
            print('Command not recognized')



def aboveBellow(compare, myList=None): # get's how many numbers in the list are above and bellow the compare
    
    if myList is None:
        myList = []
    
    above   = 0
    bellow  = 0
      
    for i in myList:
      if i < compare:
        bellow += 1

      elif i > compare:
        above += 1

      else:
        return ("this else statement should not reach here.\nIn theory\nif it does. sorry")

    # wanted to get fancy. un coment this for it to be written in a file
    # self.write(      
    #   {
    #     "above": above,
    #     "bellow": bellow
    #   }
    # )

    return json.dumps(
      {
        "above": above,
        "bellow": bellow
      }
    )


def rotateRight(data:str, rotateTimes:int) -> str: # rotate string char to the right rotateTimes times
    return data[-rotateTimes:] + data[:-rotateTimes]


def addStrings(string_A, string_B, defaultAdd='+') -> str: # adding 2 strings and returning it
    return str(f"{string_A}{defaultAdd}{string_B}")


def split(str_A:str, defaultSplit='+'): # spliting a string and returning the list
    return str_A.split(defaultSplit)

#endregion


#region basic sorting and searching
def sort(arr=None) -> list: # returns sorted list or aka array
    if arr is None:
        arr = []

    return sorted(arr)


def search(Search, arr = None) -> bool: # returning true or false if Search is found in arr
    if arr is None:
        arr = []
        
    return Search in arr


def search(Search, In) -> bool: # returning true or false if Search is found in In
    return Search in In

#endregion


def valEmail(email) -> bool: # validating if the email is valid or not
    # validating email and more
    if not re.fullmatch(REGEX, email):
        return False
    else:
        return True