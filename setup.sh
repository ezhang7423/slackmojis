#!/usr/bin/python3
import os
# from scraper import * shous stuff


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
    y = prompt("Which header would you like to download from?")
    # call shous super cool api
    # if gifs is not empty, move all files into new folder gifbak
else: 
    y = prompt("which category would you like to download from?")
    # call shous amazing api


## all data should be downloaded into gifs folder at this point
os.chdir('uploader')
os.system('python3 script.py')