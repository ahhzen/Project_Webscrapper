import requests
from pprint import pprint
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(res.text, "html.parser")

stories = soup.select(".athing")
votes = soup.select(".score")
links = soup.select(".storylink")
subtext = soup.select(".subtext")
news_list = []

for story in stories:
    news = {}
    link = story.select(".storylink")[0]
    storyid = story["id"]
    
#     print(link.text, link["href"], storyid)
    news.update({"title":link.text,"url": link["href"]})
    
    try:
        votetext = [item for item in votes if storyid in item["id"]][0]
    except IndexError:
        news.update({"score": 0})
    else:
        votetext = int(votetext.text.replace("points",""))
        news.update({"score": votetext})
    
    if news["score"] >= 100:
        news_list.append(news.copy())

news_list = sorted(news_list, key = lambda key: key["score"], reverse=True)
    
for news in news_list:
    pprint(news)
    print()
