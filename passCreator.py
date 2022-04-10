from ast import For
from colorama import Fore, Back, Style
import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "/*-+\\{}[]()<=>|_&^%$#@!?.,"
numbers = "0123456789"
all = lower + upper + symbols + numbers

while True:
    print(Fore.WHITE +"choose a option : ")
    print(Fore.GREEN + "1) Create a password\n2) Exit")
    choice = input(Fore.MAGENTA + "Enter a choose :")
    if choice == "1":
        length = int(input("Enter a lentght of password : "))
        password = "".join(random.sample(all, length))
        print("password : ",Fore.YELLOW + password)
        print("-"*40)
    elif choice == "2":
        break
    else:
        print(Fore.RED + "Choose Invalid!")
