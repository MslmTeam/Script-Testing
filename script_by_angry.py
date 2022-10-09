import sqlite3,time,os,sys,random
def text(x):
    for i in x+'\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.008)

keys = ["gb33","atees25","spangry8","keykeyan8","samole8","desolier885","porlers236","ffzsda9","packyour22"]


print("  __  __    _____   _        __  __     _______   ______              __  __ ")
print(" |  \/  |  / ____| | |      |  \/  |   |__   __| |  ____|     /\     |  \/  |")
print(" | \  / | | (___   | |      | \  / |      | |    | |__       /  \    | \  / |")
print(" | |\/| |  \___ \  | |      | |\/| |      | |    |  __|     / /\ \   | |\/| |")
print(" | |  | |  ____) | | |____  | |  | |      | |    | |____   / ____ \  | |  | |")
print(" |_|  |_| |_____/  |______| |_|  |_|      |_|    |______| /_/    \_\ |_|  |_|")

text("To use this script, you must obtain a key")
text("But since we are a Muslim team")
text("We have created a game for you")
text("If you win the game you will earn a free key")
text("")
text("Greetings to you from the Muslim team")

text("[1] Enter My Key")
text("[2] Play For Get Your Key")
text("[0] Exit")

coise = input("Enter Your choise : ")
if coise=="1":
    key = input("Enter Your Key To Start Script : ")
    if key in keys:
        text("Your key is on")
        import os,time,sys

    try:
        import requests
    
    except:
        os.system("pip install requests")
        os.system("clr")
        os.system("python script_by_angry.py")

    print("")
    text("[1] UPDATE MY SCRIPT")
    text("[2] SHOW MY IP INTERNET")
    text("[3] WIRLOS INFORMATION")
    text("[4] INFORMATION ANGRY")
    text("[0] EXIT")
    print("")
    choise = input("Enter Choise : ")

    if choise=="1":
        os.system("cls")
        text("The Option Is Not Font(BETA)")
        os.system("python script_by_angry.py")
    elif choise=="2":
        os.system("cls")
        try:
            print(requests.get("https://api.ipify.org/").text.split())
        except:
            text("No Internt In Your PC!")
        os.system("python script_by_angry.py")
    elif choise=="3":

        os.system("cls")
        print(os.system("ipconfig"))
        os.system("python script_by_angry.py")
    elif choise=="4":
        os.system("cls")
        text("MY DISCORD : ANGRY 444#6139")
        text("MY TEAM : MSLM TEAM")
        text("PERSON TEAM : ANGRY    EXP    EL9IRCH")
        text("EXPERIONT TEAM : PROGRAMING PYTHON AND HACKING KALI LINUX")
        text("AND SECRUTY SET WEB")
    if choise=="0":
        os.system("cls")
        sys.exit()
    else:
    
        text("Plese Select 1 Or 2 Or 3 Or 0 For Exit!")
        os.system("python script_by_angry.py")



elif coise=="2":
    text("Ok Lets GO!")
    text("You have calculations that you must calculate yourself")
    text("Each operation = key")
    print("")
    n1 = random.randint(5,150)
    print(n1)
    print("+")
    n2 = random.randint(5,199)
    print(n2)
    print("")
    resrobot = n1+n2
    resuser = input("What is the result ? : ")
    if int(resuser)==resrobot:
        text("Nice I got a key")
        text("Your Key is : "+random.choice(keys))
    
if coise=="3":
    exit()


