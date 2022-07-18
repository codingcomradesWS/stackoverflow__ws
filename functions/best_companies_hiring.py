import requests
from bs4 import BeautifulSoup


def get_best_companies_hiring(topic):
    """
            This function gets the best 10 companies which is hiring a developers with a specific programming language
            :param topic: the programming language or the topic
            :return: list of companies names
    """
    r = requests.get(f'https://stackoverflow.com/jobs/companies?tl={topic}')
    soup = BeautifulSoup(r.content, 'html.parser')
    companies = soup.findAll('div', class_='flex--item fl1 text mb0')
    best_10_companies = []
    for c in companies:
        if len(best_10_companies) < 10:
            title = c.find('a', class_='s-link')
            # print(title)
            best_10_companies.append({"Title": title.getText(), "Link": f"https://stackoverflow.com{title.get('href')}"})
    return best_10_companies


if __name__ == "__main__":
    print(get_best_companies_hiring("python"))
