from os import system
from exif import Image
from time import sleep
print("Mahdi Tavazohi")
print("Please wait 3 seconds.")
sleep(1)
system('cls')
print("Mahdi Tavazohi")
print("Please wait 2 seconds.")
sleep(1)
system('cls')
print("Mahdi Tavazohi")
print("Please wait 1 seconds.")
sleep(1)
system('cls')
print("next page ...")
sleep(1)
system("cls")
print("\033[4m\033[1;31mTo search, make sure the folder or file name is in English only.\n\nOtherwise you will encounter an error.To enter the address, you can enter the address manually or drag and drop the file on the console.\033[0m\n")
picture=input("Picture Address :")
system("cls")
try:
    img=Image(open(picture,"rb"))
    software=img.software
    model=img.model
    time=img.datetime
    print("\033[0;37mModel : \033[1;31m%s\n\033[0;37msoftware : \033[1;31m%s\n\033[0;37mShooting time : \033[1;31m%s\n"%(model,software,time))
    q=input("""\033[1;36myes = model search and clear page.
press enter = exit in page.
Give me yes or press enter :""")
    q=q.upper()
    if q=="YES" or q=="Y":
        system("cls")
        system("start https://www.google.com/search?q=%s"%(model))
    else:
        pass
except FileNotFoundError:
    print("Your photo could not be found!")
    input()







 
