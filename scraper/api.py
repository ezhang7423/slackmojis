import requests
import re
import os
import shutil


def cleargif():
    for file in os.listdir('gifs'):
        shutil.move(f'gifs/{file}', f'gifbak/{file}')


def getCategory(url):
    cleargif()
    a = requests.get(url).content.replace(b"\n", b"")
    c = re.compile(b"href=\"(.+?)\"").findall(a)
    for i in c:
        fn = i.split(b"/")[-2].split(b"-")[-1]
        with open("gifs/%s.gif" % fn.decode("utf-8"), "wb") as p:
            if b"emojis" not in i:
                continue
            print(str(i))
            p.write(requests.get("https://slackmojis.com%s" %
                                 i.decode("utf-8")).content)
    os.remove('gifs/.gif')
    os.remove('gifs/categories.gif')
    os.remove('gifs/assets.gif')


def getHeader(name):
    cleargif()
    a = requests.get("https://slackmojis.com/").content.replace(b"\n", b"")
    v = re.compile(
        b"<div class='title'>%s</div>(.+?)<div class='title'>" % name)
    try:
        u = v.findall(a)[0]
    except:
        return []
    c = re.compile(b"href=\"(.+?)\"").findall(u)
    for i in c:
        fn = i.split(b"/")[-2].split(b"-")[-1]
        with open("gifs/%s.gif" % fn.decode("utf-8"), "wb") as p:
            print(str(i))
            p.write(requests.get("https://slackmojis.com%s" %
                                 i.decode("utf-8")).content)
