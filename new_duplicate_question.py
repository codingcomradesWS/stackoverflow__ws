import requests
from bs4 import BeautifulSoup


def most_active_community():
    data = requests.get("https://stackoverflow.com/tags?tab=popular")
    soup = BeautifulSoup(data.content, 'html.parser')
    communities = soup.select("div.grid--item a")
    print(f"{communities[0].contents[0]} community is most active community in stack-over-flow")

def new_duplicate_question(question):
    data = requests.get("https://stackoverflow.com/tags?tab=popular")


if __name__ == '__main':
    pass
