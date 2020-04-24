#!/usr/bin/python3
import os
from scraper.api import *


def prompt(query):
    y = input(query + '\n')
    while y != 'y' and y != 'n':
        print("That's not a valid option.")
        y = input(query + '\n')
    return y

y = prompt("Have you set credentials yet? (y/n)")
if y == 'n':
    ss = input("What's the url of your slack site? e.g. https://shouandeddie.slack.com/\n")
    email = input("What's your email?\n")
    password = input("What's your password? This information stays only on your computer.\n")
    with open('uploader/.env', 'w') as fout:
        fout.write(f"SLACKSITE={ss}customize/emoji\n")
        fout.write(f"EMAIL={email}\n")
        fout.write(f"PASSWORDD={password}\n")



os.system('python3 -mwebbrowser https://slackmojis.com/')
y = prompt("Would you like to download off of the main page?")  
if y == 'y':
    f = input("Which header would you like to download from? e.g. 'Star Wars'\n")
    getHeader(f.encode('utf-8'))
    # if gifs is not empty, move all files into new folder gifbak
else: 
    f = input("which category would you like to download from? e.g. 'https://slackmojis.com/emojis/popular' or 'https://slackmojis.com/categories/17-hangouts-blob-emojis'\n")
    # call shous amazing api
    getCategory(f.encode('utf-8'))


## all data should be downloaded into gifs folder at this point
os.chdir('uploader')
os.system('python3 script.py')