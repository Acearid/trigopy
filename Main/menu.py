from subprocess import call

def input1():
    call(["python", "./main/förstauppgift.py"])

def input2():
    call(["python", "./main/andra.py"])
def input3():
    call(["python", "./main/tredje.py"])
def input4():
    call(["python", "./main/fjärde.py"])


def print_menu():
    print("-----------------------------")
    print("[1] Avståndet mellan stjärnor")
    print("[2] Avståndet mellan jorden och stärna")
    print("[3] Höjden av ett träd")
    print("[4] Vilket bärg är störst")
    print("[5] Exit")
    print("-----------------------------")
def mainfunc():
    print("""

                  _   _                               _  __ _             
                 | | | |                             (_)/ _| |            
  _ __ ___   __ _| |_| |_ ___ _   _ _ __  _ __   __ _ _| |_| |_ ___ _ __  
 | '_ ` _ \ / _` | __| __/ _ \ | | | '_ \| '_ \ / _` | |  _| __/ _ \ '_ \ 
 | | | | | | (_| | |_| ||  __/ |_| | |_) | |_) | (_| | | | | ||  __/ | | |
 |_| |_| |_|\__,_|\__|\__\___|\__,_| .__/| .__/ \__, |_|_|  \__\___|_| |_|
                                   | |   | |     __/ |                    
                                   |_|   |_|    |___/                     
""")
    print_menu()
    option = input("val >> ")
    if option == "1":
        input1()
    elif option == "2":
        input2()
    elif option == "3":
        input3()
    elif option == "4":
        input4
    elif option == "5":
        exit()

while 1:
    mainfunc()
