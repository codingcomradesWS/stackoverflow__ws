import random
import time
import requests
from bs4 import BeautifulSoup


def delay(x, y):
    time.sleep(random.randint(x, y))


def get_recent_questions(url):
    standard_link_start = "https://stackoverflow.com"
    search_format = input("search for tag: ").split(" ")
    res = requests.get(url + "-".join(search_format) + "?sort=Newest&edited=true")
    soup = BeautifulSoup(res.content, 'html.parser')
    test = soup.select('div.s-post-summary.js-post-summary > div.s-post-summary--content > h3')
    for i in range(10):
        print("\n----------------------\n")
        print("Title: ", test[i].get_text())
        print("Link: ", f"{standard_link_start}{test[i].select('a')[0].get('href')}")


if __name__ == "__main__":
    url_start = "https://stackoverflow.com/questions/tagged/"
    # url_start = "https://stackoverflow.com/search?q=how to join array elements"
    # url_start = "https://stackoverflow.com/nocaptcha?s=7334ebe7-3c56-4baa-bb23-3ec21fadb254"
    # url_start = "https://google.com/recaptcha/api2/demo"
    # get_recent_questions(url_start)
    get_recent_questions(url_start)
