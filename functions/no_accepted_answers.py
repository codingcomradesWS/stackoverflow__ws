import requests
from bs4 import BeautifulSoup


def get_questions_with_no_accepted_answers(topic, number_of_questions=10):
    """
        This function gets the most questions that have no accepted answers, the number of returned questions is specified by the passed number.
        :param topic: the name of the topic/tag
        :param number_of_questions: the requested number of questions
        :return: list of dictionaries
        """
    if number_of_questions > 50:
        number_of_questions = 50
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
    questions = soup.select("div.s-post-summary.js-post-summary")
    questions_list = []
    standard_link_start = "https://stackoverflow.com"
    for q in questions:
        if len(questions_list) < number_of_questions:
            questions_list.append({"Title": q.select("div.s-post-summary--content > h3")[0].get_text(),
                                   "Link": f"{standard_link_start}{q.select('a')[0].get('href')}",
                                   "NumberOfAnswers": q.select("div.s-post-summary--stats-item")[1].get("title")})

    return questions_list


if __name__ == '__main__':
    print(get_questions_with_no_accepted_answers('html css'))
    # print(get_questions_with_no_accepted_answers('python'))
