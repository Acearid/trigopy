from subprocess import call

red = '\33[91m'
white = '\33[0m'
blue = '\33[96m'
def input1():
    call(["python", "förstav2.py"])
def input2():
    call(["python", "andra.py"])
def input3():
    call(["python", "tredje.py"])
def input4():
    call(["python", "fjärde.py"])


def print_menu():
    print("-----------------------------")
    print(blue + "[1]" + white + "Avståndet mellan stjärnor")
    print(blue + "[2]" + white +  "Avståndet mellan jorden och stärna")
    print(blue + "[3]" + white + "Höjden av ett träd")
    print(blue + "[4]" + white + "Vilket bärg är störst")
    print(blue + "[5]" + white + "Exit")
    print("-----------------------------")

def mainfunc():
    print(red +"""

                  _   _                               _  __ _             
                 | | | |                             (_)/ _| |            
  _ __ ___   __ _| |_| |_ ___ _   _ _ __  _ __   __ _ _| |_| |_ ___ _ __  
 | '_ ` _ \ / _` | __| __/ _ \ | | | '_ \| '_ \ / _` | |  _| __/ _ \ '_ \ 
 | | | | | | (_| | |_| ||  __/ |_| | |_) | |_) | (_| | | | | ||  __/ | | |
 |_| |_| |_|\__,_|\__|\__\___|\__,_| .__/| .__/ \__, |_|_|  \__\___|_| |_|
                                   | |   | |     __/ |                    
                                   |_|   |_|    |___/                     
 """ + white)
    print_menu()
    option = input("val >> ")
    if option == "1":
        input1()
    elif option == "2":
        input2()
    elif option == "3":
        input3()
    elif option == "4":
        input4()
    elif option == "5":
        exit()

while 1:
    mainfunc()
