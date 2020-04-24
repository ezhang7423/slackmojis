import requests
import re


def f1(url):
    a = requests.get(url).content.replace(b"\n", b"")
    c = re.compile(b"href=\"(.+?)\"").findall(a)
    for i in c:
        fn = i.split(b"/")[-2].split(b"-")[-1]
        with open("../gifs/%s.gif" % fn.decode("utf-8"), "wb") as p:
            if b"emojis" not in i:
                continue
            print(str(i))
            p.write(requests.get("https://slackmojis.com%s" %
                                 i.decode("utf-8")).content)


def f2(name):
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
        with open("../gifs/%s.gif" % fn.decode("utf-8"), "wb") as p:
            print(str(i))
            p.write(requests.get("https://slackmojis.com%s" %
                                 i.decode("utf-8")).content)


# print(f1(b"https://slackmojis.com/categories/17-hangouts-blob-emojis"))
print(f2(b"Star Wars"))
