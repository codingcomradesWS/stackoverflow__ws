import requests
from bs4 import BeautifulSoup

def get_developers_on_stackoverflow():
    """
    This function is finding what kinds of developers visit Stack Overflow and the percentage
    :return: the percentage and the kind of developers
    """
    r = requests.get("https://stackoverflow.co/advertising/audience")
    soup = BeautifulSoup(r.content, 'html.parser')
    percentage = soup.findAll('span', class_='fs-display3 p-ff-roboto-slab-bold va-middle mr24 ta-center flex--item3')
    devs = soup.findAll('span', class_='fc-black-600 fs-body3')
    result = []
    for p in percentage:
        result.append({
            'percentage': p.getText()
        })
    result2 =[]
    for d in devs:
        result2.append(d.getText())
    result[0]['type of developers'] = result2[0]
    result[1]['type of developers'] = result2[1]
    return result
