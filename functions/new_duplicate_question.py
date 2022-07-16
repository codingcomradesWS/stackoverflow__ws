import requests
from bs4 import BeautifulSoup


def new_duplicate_question(questions_list):
    """
    This function accepts a list of dictionaries
    :param questions_list:
    :return: text including the original question and the link for it
    """
    for i in questions_list:
        if "[duplicate]" in i["Title"]:
            original_question = requests.get(i["Link"])
            soup = BeautifulSoup(original_question.content, 'html.parser')
            if str(soup).find("This question already has answers here") != -1:
                notification = soup.select('aside a')
                print( f"- {i['Title']} \nduplicated question from the original question \"{notification[0].contents[0]}\" \n original question link https://stackoverflow.com{notification[0]['href']}")
            else:
                notification = soup.select('#question-header h1 a')
                print( f"- {i['Title']} \nduplicated question from the original question \"{notification[0].contents[0]}\" \n original question link is {i['Link']}")


if __name__ == '__main__':
    array = [{"Title": "Is grid something defined on the JavaScript language? [duplicate]",
              "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"},
             {"Title": "Is grid something defined on the JavaScript language? ",
              "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"}
             ]
    print(new_duplicate_question(array))
