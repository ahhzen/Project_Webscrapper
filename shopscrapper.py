from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pprint import pprint

chrome_option = Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--window-size=1920x1080")

browser = webdriver.Chrome(options=chrome_option)
browser.get("https://shopee.com.my/Computer-Accessories-cat.174?page=0&ratingFilter=4&sortBy=sales")

soup = BeautifulSoup(browser.page_source, "html.parser")

boxes = soup.select("._1gkBDw")

for box in boxes:
    item = {}
    boxsales = box.select("._18SLBt")[0]
    
    desc = box.select(".O6wiAW")[0]
    price_unit = box.select(".lwZ9D8")[0]
    price_low = box.select("._341bF0")[0]
    location = box.select("._3amru2")[0]
    
    item.update({"name": desc.text, 
                 "sales": boxsales.text, 
                 "price": price_unit.text + price_low.text, 
                 "location": location.text})
    pprint(item)
