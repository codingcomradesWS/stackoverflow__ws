import json
from stackapi import StackAPI


def get_search_results(q_text, tag, number_of_results):
    SITE = StackAPI('stackoverflow')
    SITE.page_size = number_of_results
    SITE.max_pages = 1
    search_results = SITE.fetch('search/advanced', q=q_text, tgged=tag)
    # print(json.dumps(search_results["items"], indent=4))
    returned_results = [{"Title": i["title"], "Link": i["link"]} for i in search_results["items"]]
    return returned_results


def get_most_voted_results(tag, number_of_results):
    SITE = StackAPI('stackoverflow')
    SITE.page_size = number_of_results
    SITE.max_pages = 1
    search_results = SITE.fetch('questions', sort="votes", tgged=tag)
    returned_results = [{"Title": i["title"], "Link": i["link"], "Votes": i["score"]} for i in search_results["items"]]
    # print(json.dumps(returned_results, indent=4))
    return returned_results


# if __name__ == "__main__":
#     print(get_search_results("How to split a list in python", "python", 10))
#     print(get_most_voted_results("python", 5))
