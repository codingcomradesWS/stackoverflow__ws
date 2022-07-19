import requests
from bs4 import BeautifulSoup


def new_duplicate_question(questions_list):
    """
    This function accepts a list of dictionaries
    :param questions_list:
    :return: text including the original question and the link for it
    """
    
    if "[duplicate]" in questions_list["Title"]:
        original_question = requests.get(questions_list["Link"])
        soup = BeautifulSoup(original_question.content, 'html.parser')
        if str(soup).find("This question already has answers here") != -1:
            notification = soup.select('aside a')
            # return f"- {i['Title']} \nduplicated question from the original question \"{notification[0].contents[0]}\" \n original question link https://stackoverflow.com{notification[0]['href']}"
            return {"Title": notification[0].contents[0],
                    "Link": f"https://stackoverflow.com{notification[0]['href']}"}
        else:
            notification = soup.select('#question-header h1 a')
            # return f"- {i['Title']} \nduplicated question from the original question \"{notification[0].contents[0]}\" \n original question link is {i['Link']}"
            return {"Title": notification[0].contents[0],
                    "Link": f"{questions_list['Link']}"}
    else:
        return


if __name__ == '__main__':  # pragma: no cover
    array = {"Title": "Is grid something defined on the JavaScript language? [duplicate]",
              "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"}

    print(new_duplicate_question(array))
