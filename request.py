import requests
from requests import get

response = get(
    "https://sanantonio.craigslist.org/search/cta?query=sprinter&hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=15&nearbyArea=265&nearbyArea=647&nearbyArea=327&nearbyArea=449&nearbyArea=564"
)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, "html.parser")

posts = html_soup.find_all("li", class_="result-row")
print(type(posts))
print(len(posts))

post_title_texts = []
post_price = []
post_links = []
post_date = []
post_timing = []

for post in posts:
    # post dates
    post_datetime = post.find("time", class_="result-date")["datetime"]
    post_timing.append(post_datetime)

    # titles
    post_title = post.find("a", class_="result-title hrdlnk")
    post_title_text = post_title.text
    post_title_texts.append(post_title_text)

post_one = posts[0]
post_one_dict = {}

post_one_dict["title"] = post_one.find("a", class_="result-title hdrlnk").text
post_one_dict["price"] = post_one.find("span", class_="result-price").text
post_one_dict["date"] = post_one.find("time", class_="result-date").text
post_one_dict["location"] = post_one.find("span", class_="nearby").text
