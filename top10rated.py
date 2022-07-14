import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/users?tab=Reputation&filter=all"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="user-browser")

box = soup.select("div.grid--item")

starter_link = "https://stackoverflow.com"

#print(box)

for i in range(10):
    #print(box[i].select("div.-flair"))
    print("------------------------------------------")
    print(box[i].select("div.user-details a")[0].contents[0])
    print(f"{starter_link}{box[i].select('div.user-gravatar48 > a')[0].get('href')}")
    print("------------------------------------------")

    #print(box[i].select("span.reputation-score"))

