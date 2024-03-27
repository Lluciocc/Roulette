import os

def launchTool():
    tool = input("Do you want to launch the tool ? (y/n)    >>>")
    if tool == "y":
        print("Tool started")
        os.system("python index.py")
    elif question == "n":
        return
    else:
        return

while True:
    question  = input("install requirements ? (y/n)    >>>")

    if question == "y":
        print("UPGRADING PIP")
        os.system("python3 -m pip install --upgrade pip")
        print("INSTALL REQUIREMENTS")
        os.system("pip install pystyle")
        os.system("pip install time")
        print("Requirements install sucefully !")
        launchTool()
           
    elif question == "n":
        break
    else: 
        print("just y or n")
        os.system("python requirements.py")
