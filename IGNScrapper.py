from bs4 import BeautifulSoup
import requests

# url = "https://sea.ign.com/"
url = "https://sea.ign.com/?page=1&ist=broll"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# articles = soup.find_all("article")
articles = soup.select("article.article.NEWS")
art_list = []

for article in articles:
    link = article.select(".thumb.score-wrapper")[0]
    title = article.find("h3")
    article_dict = {}
    article_dict.update({"title": title.text, "url": link["href"]})
    art_list.append(article_dict.copy())
    
from pprint import pprint

for num, article in enumerate(art_list):
    print(num, end=" ")
    pprint(article)
    print()
