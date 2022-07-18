import requests
from bs4 import BeautifulSoup
import re


def most_active_community():
    """
    This function returns a report of the most active community for this week on stack overflow, using the number of
    asked questions for the week as a base.
    :return: string
    """
    communities_array = []
    data = requests.get("https://stackoverflow.com/tags")
    soup = BeautifulSoup(data.content, 'html.parser')
    max_weekly = 0
    weekly_active_community = ""
    communities = soup.select(".grid--item a")

    for j in range(len(communities)):
        if communities[j].contents[0].find("week") != -1:
            weekly_questions = re.findall(r'\d+', communities[j].contents[0])
            weekly_active_community1 = \
            str(communities[j])[str(communities[j]).find("questions tagged") + len("questions tagged"):].split()[0]
            community_dict = {"community": weekly_active_community1, "max_weekly": int(weekly_questions[0])}
            communities_array.append(community_dict)
            if int(weekly_questions[0]) > max_weekly:
                max_weekly = int(weekly_questions[0])
                weekly_active_community = \
                str(communities[j])[str(communities[j]).find("questions tagged") + len("questions tagged"):].split()[0]
    # print(communities_array)

    return f"most active community is {weekly_active_community} with {max_weekly} questions per week "


# if __name__ == "__main__":
#     print(most_active_community())
