
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
import wsl
import platform


def getQA(name):
    sel = f"[data-qa={name}]"
    return driver.find_element_by_css_selector(sel)


load_dotenv(verbose=True)
gifpath = os.path.join(os.path.split(os.getcwd())[0], 'gifs')
gifs = os.listdir(gifpath)
paths = [os.path.join(gifpath, x) for x in gifs]
if platform.system() == 'Linux':
    if not os.system('grep -q Microsoft /proc/version'):
        # wsl
        paths = [wsl.convert_w(path) for path in paths]
        cp = 'chromedriver.exe'
    else:
        cp = 'chromedriver'
elif platform.system() == 'Darwin':
    cp = 'mchromedriver'
else:
    cp = 'chromedriver.exe'


driver = Chrome(executable_path=os.path.join(os.getcwd(), cp))
driver.get(os.environ['SLACKSITE'])


driver.find_element_by_css_selector("#email").send_keys(os.environ['EMAIL'])
driver.find_element_by_css_selector(
    "#password").send_keys(os.environ['PASSWORDD'])
driver.find_element_by_css_selector("#password").send_keys(Keys.ENTER)


time.sleep(3)
for x in range(len(paths)):
    try:
        getQA('customize_emoji_add_button').click()
        time.sleep(.1)
        getQA('customize_emoji_add_dialog_file_input').send_keys(paths[x])
        driver.find_element_by_id('emojiname').send_keys(gifs[x].split('.')[0])
        getQA('customize_emoji_add_dialog_go').click()
    except:
        try:
            getQA('customize_emoji_add_dialog_close').click()
        except NoSuchElementException:
            continue
