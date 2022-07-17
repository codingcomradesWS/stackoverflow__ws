import requests
from bs4 import BeautifulSoup


def unanswered_questions_percentage():
    """
     this function will get the unanswered question's percentage for the top 10 tags in stack overflow
     in daily basis, weekly basis, and All time
    :params: None
    :return: list of dictionaries
    """
    tags = []
    unanswered_percentage = []
    tags_data = requests.get("https://stackoverflow.com/tags")
    soup = BeautifulSoup(tags_data.content, 'html.parser')
    targeted_tags = soup.select('.post-tag')
    for tag in targeted_tags:
        tags.append(tag.contents[0])

    for i in range(10):
        if tags[i] == "c#":
            tags[i] = 'c%23'
        tag_info = requests.get(f"https://stackoverflow.com/tags/{tags[i]}/topusers")
        if tags[i] == 'c%23':
            tags[i] = 'c#'
        tag_info_formated = BeautifulSoup(tag_info.content, 'html.parser')
        unanswered_questions = tag_info_formated.select('.fc-black-500.py8')
        unanswered_percentage.append(
            {'tag': tags[i],
             'unanswered_7days': unanswered_questions[0].contents[0],
             'unanswered_30days': unanswered_questions[1].contents[0],
             'unanswered_all_time': unanswered_questions[2].contents[0]}
        )
    return unanswered_percentage


if __name__ == "__main__":
    x = unanswered_questions_percentage()
    print(list(x[0].keys()))
