#! /usr/bin/python3
# coding=utf-8

import colorama
from colorama import Fore, Back, Style
from BANNER import banner
import random
import string
import os
from time import sleep

colorama.init(autoreset=True)

#try:
    #os.system("cp main.py /usr/local/bin/")
#except Exception as e:
    #print(e)
    #exit()
print(f"{Fore.GREEN}___________________________________PASSWORD GENERATOR________________________________________           ")
print("\n")
print("[GIVE ANSWER IN YES(Y),NO(N) FORMAT]")
print("\n")
lowercase = string.ascii_lowercase
uppercase=string.ascii_uppercase
num=string.digits
punctuation=('@#$%.')
#print(lowercase)
#print(punctuation)
words=[]
def func(l,var2):
    while True:
        if l=="y":
            words.extend(list(var2))
            break
        elif l=="n":
            break
        elif l=="Y":
            words.extend(list(var2))
            break
        elif l=="N":
            break
        else:
            print("[+]YOU ENTER A WRONG INPUT")
            l=input(f"{Fore.BLUE}>>>")
        
print("\n")
L=input(f"{Fore.BLUE}[+]DO YOU WANT LOWERCASE WORD IN YOUR PASSWORD: ")
func(L,lowercase)
print("\n")
U=input(f"{Fore.BLUE}[+]DO YOU WANT UPPERCASE WORDS IN YOUR PASSWORD: ")
func(U,uppercase)
print("\n")
S=input(f"{Fore.BLUE}[+]DO YOU WANT SPECIAL CASE WORDS IN YOUR PASSWORD: ")
func(S,punctuation)
print("\n")
N=input(f"{Fore.BLUE}[+]DO YOU WANT NUMBERS IN YOUR PASSWORD: ")
func(N,num)
print("\n")


while True:
    try:
        size=int(input(f"{Fore.BLUE}[+]ENTER THE SIZE OF THE PASSWORD: "))
        break
    except:
        print(f"{Fore.RED}[+]YOU ENTER A WORD INSTEAD OF NUMBER,TRYAGAIN")
        
print("\n")
name=input(f"{Fore.BLUE}[+]ENTER FOR WHAT YOU USED THIS PASSWORD: ")

print("\n")
random.shuffle(words)
key=random.sample(words,size)
j="".join(key)
for i in key:
    print(f"{Fore.RED}[+]CHOOSING WORDS FROM YOUR PASSWORD LIST,PLEASE WAIT",list(i))
    sleep(1)

sleep(1)
print(f"{Fore.RED}[+]GENERATING YOUR PASSWORD,PLEASE WAIT\n")
sleep(1)
print(f'''[-]CHOOSEN PASSWORD FOR YOU IS{Fore.GREEN}"{j}"''')
print("\n")
save=input(f"{Fore.GREEN}DO YOU WANT TO SAVE YOUR PASSWORD IN A FILE: ")

try:
    os.chdir("password")
except:
    os.mkdir("password")
    os.chdir("password")
    
if save=="y":
    f=input("ENTER FILENAME: ")
    filename=str(f)+".txt"
    with open(filename,"a") as f:
            f.write("\n")
            f.write(f"{j} = {name}")
            print(f'''{Fore.GREEN}YOUR PASSWORD IS STORED IN "password/{filename}" FILE!''')
            print(f"{Fore.GREEN}THANKS FOR USING OUR SEVICE,SEE YOU LATER!")
elif save=="n":
    print(f"{Fore.GREEN}THANKS FOR USING OUR SEVICE,SEE YOU LATER!")
    exit()
else:
    print(f"{Fore.RED}YOU ENTER A WRONG INPUT BUT ANYWAYS,BYE")










