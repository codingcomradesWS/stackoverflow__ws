import requests
from bs4 import BeautifulSoup

data = requests.get("https://stackoverflow.com/tags?tab=popular")
soup = BeautifulSoup(data.content, 'html.parser')
communities = soup.select("div.grid--item a")
print(f"{communities[0].contents[0]} community is most active community in stack-over-flow")
