import requests
from bs4 import BeautifulSoup


def highest_rated_answers(tag):
    req = requests.get(f'https://stackoverflow.com/questions/tagged/{tag}?sort=MostVotes&edited=true')
    soup = BeautifulSoup(req.content, 'html.parser')

    answers = soup.findAll('div', class_=' flush-left')
    best_10_ans = []

    # for i in answers:
    #     while len(best_10_ans) < 10:
    #         question = i.find('div', class_='s-post-summary')
    #        # print(best_10_ans[i].select("div.user-details a")[0].contents[0])
    #         best_10_ans.append(question.getText())
    #
    #         #best_10_ans.append(question.getText())
    # return best_10_ans
    print(answers)

if __name__ == '__main__':
    print(highest_rated_answers('python'))

