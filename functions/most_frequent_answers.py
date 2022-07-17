import requests
from bs4 import BeautifulSoup


def get_frequent(topic, number_of_questions=10):
    """
    This function gets the most frequent answers, the number of returned questions is specified by the passed number.
    :param topic: the name of topic
    :param number_of_questions: the requested number of most frequent answers
    :return: list of dictionaries of 1. The title of the question, 2. The link of the question
    """
    if number_of_questions > 50:
        number_of_questions = 50
    list_topic = topic.split()
    if len(list_topic) == 1:
        url = f'https://stackoverflow.com/questions/tagged/{topic}?sort=MostFrequent'
    else:
        new_topic = f'{list_topic[0]}'
        list_topic.pop(0)
        for i in range(len(list_topic)):
            new_topic = new_topic + "%20" + list_topic[i]
        url = f'https://stackoverflow.com/questions/tagged/{new_topic}?sort=MostFrequent'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    questions = soup.findAll("div", class_="s-post-summary js-post-summary")
    first_ten_questions = []
    for q in questions:
        if len(first_ten_questions) < number_of_questions:
            question_link = 'https://stackoverflow.com/' + q.a['href']
            first_ten_questions.append(
                {
                    "Title": q.find('a', class_='s-link').getText(),
                    "Link": question_link
                }
            )
    return first_ten_questions


if __name__ == '__main__':
    print(get_frequent('python', 20))
