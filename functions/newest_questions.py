import requests
from bs4 import BeautifulSoup


def get_recent_questions(user_input, num_of_questions=10):
    """
    This function gets the most recent questions, the number of returned questions is specified by the passed number.
    :param user_input: the name of the topic/tag
    :param num_of_questions: the requested number of questions
    :return: list of dictionaries
    """
    if num_of_questions > 50:
        num_of_questions = 50
    output = []
    standard_link_start = "https://stackoverflow.com"
    search_format = user_input.split(" ")
    res = requests.get("https://stackoverflow.com/questions/tagged/" + "-".join(search_format) + "?sort=Newest&edited=true")
    soup = BeautifulSoup(res.content, 'html.parser')
    question_container = soup.select('div.s-post-summary.js-post-summary > div.s-post-summary--content')
    for i in range(num_of_questions):
        output.append({"Title": question_container[i].select("h3")[0].get_text(),
                       "Link": f"{standard_link_start}{question_container[i].select('a')[0].get('href')}",
                       "Date&Time": question_container[i].select("time.s-user-card--time")[0].get_text()})
    return output


if __name__ == "__main__":
    # print(len(get_recent_questions("python", 30)))
    # print(get_recent_questions("python", 30))
    test()
