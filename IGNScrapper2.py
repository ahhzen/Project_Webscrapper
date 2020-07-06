from bs4 import BeautifulSoup
from pprint import pprint
import requests

# url = "https://sea.ign.com/"
url = "https://sea.ign.com/?page=1&ist=broll"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("article")
title_text = ""

artlist = []
for article in articles:
    links = []
    imgs = []
    videos = []
    try:
        title = article.find_all("h3")
        if len(title) > 0:
            title_text = title[0].text
        else:
            title = article.find_all("h2")
            if len(title) > 0:
                title_text = title[0].text
        links = article.find_all("a")
        imgs = article.find_all("img")
        videos = article.find_all("iframe")
    except:
         pass
    
    artdict = {"title": title_text}
    if len(videos) > 0:
        video = videos[0]
        artdict.update({"video": video["src"]})
    if len(links) > 0:
        link = links[0]
        artdict.update({"url": link["href"]})
    if len(imgs) > 0:
        img = imgs[0]
        artdict.update({"image": img["src"]})
    artlist.append(artdict.copy())

for art in artlist:
    pprint(art)
    print()
