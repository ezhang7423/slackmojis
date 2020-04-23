# To add a new cell, type ''
# To add a new markdown cell, type ' [markdown]'

import subprocess
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
import wsl


def getQA(name):
    sel = f"[data-qa={name}]"
    return driver.find_element_by_css_selector(sel)


load_dotenv(verbose=True)
gifpath = os.path.join(os.path.split(os.getcwd())[0], 'gifs')
gifs = os.listdir(gifpath)
paths = [os.path.join(gifpath, x) for x in gifs]
if os.name == 'posix':
    if not os.system('grep -q Microsoft /proc/version'):
        paths = [wsl.convert_w(path) for path in paths]


driver = Chrome(executable_path='./chromedriver.exe')
driver.get(os.environ['SLACKSITE'])


driver.find_element_by_css_selector("#email").send_keys(os.environ['EMAIL'])
driver.find_element_by_css_selector(
    "#password").send_keys(os.environ['PASSWORDD'])
driver.find_element_by_css_selector("#password").send_keys(Keys.ENTER)


time.sleep(3)
for x in range(len(paths)):
    getQA('customize_emoji_add_button').click()
    time.sleep(.1)
    getQA('customize_emoji_add_dialog_file_input').send_keys(paths[x])
    driver.find_element_by_id('emojiname').send_keys(gifs[x].split('.')[0])
    getQA('customize_emoji_add_dialog_go').click()
