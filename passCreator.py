from colorama import Fore, Back, Style
import pyfiglet

import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "/*-+\\{}[]()<=>|_&^%$#@!?.,"
numbers = "0123456789"
all = lower + upper + symbols + numbers
print(pyfiglet.figlet_format("Pass Creator"))
while True:
    print(Fore.WHITE +"choose a option : ")
    print(Fore.GREEN + "1) Create a password\n2) Exit\n3) Help")
    choice = input(Fore.MAGENTA + "Enter a choose :")
    if choice == "1":
        length = int(input("Enter a lentght of password : "))
        password = "".join(random.sample(all, length))
        print("password : ",Fore.YELLOW + password)
        print("-"*40)
    elif choice == "2":
        break
    elif choice == "3":
        print("1)-> create a pass \n 2)-> enter a lengrh pass \n3)-> printed pass")
    else:
        print(Fore.RED + "Choose Invalid!")
