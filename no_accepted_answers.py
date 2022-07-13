import requests
from bs4 import BeautifulSoup


def get_questions_with_no_accepted_answers(topic):
    list_topic = topic.split()
    if len(list_topic) == 1:
        url = f'https://stackoverflow.com/questions/tagged/{topic}?sort=Newest&filters=NoAcceptedAnswer'
    else:
        new_topic = f'{list_topic[0]}'
        list_topic.pop(0)
        for i in range(len(list_topic)):
            new_topic = new_topic + "%20" + list_topic[i]
        url = f'https://stackoverflow.com/questions/tagged/{new_topic}?sort=Newest&filters=NoAcceptedAnswer'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    questions = soup.findAll("div", class_="s-post-summary js-post-summary")
    first_ten_questions = []
    for q in questions:
        if len(first_ten_questions) < 10:
            question_link = 'https://stackoverflow.com/' + q.a['href']
            first_ten_questions.append(question_link)
    return first_ten_questions


if __name__ == '__main__':
    print(get_questions_with_no_accepted_answers('html css'))
