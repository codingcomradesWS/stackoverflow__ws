from functions.stack_api import *


def test_that_search_and_high_vote_results_are_returned():
    assert get_search_results("how to create a variable", "javascript", 10)[0]["Title"] is not None
    assert get_search_results("how to create a variable", "javascript", 10)[0]["Link"] is not None \
           and get_search_results("how to create a variable", "javascript", 10)[0]["Link"].startswith(
        'https://stackoverflow.com/questions')
    assert get_most_voted_results("python", 10)[0]["Title"] is not None
    assert get_most_voted_results("javascript", 10)[0]["Link"] is not None \
           and get_most_voted_results("javascript", 10)[0]["Link"].startswith(
        'https://stackoverflow.com/questions')
    assert get_most_voted_results("javascript", 10)[0]["Votes"] is not None


def test_the_returned_data_types():
    assert type(get_search_results("how to create a variable", "javascript", 5)) == type([]) \
           and type(get_most_voted_results("python", 5)) == type([])
    assert type(get_search_results("how to create a variable", "javascript", 5)[0]["Title"]) == type("") \
           and type(get_most_voted_results("python", 5)[0]["Title"]) == type("")
    assert type(get_search_results("how to create a variable", "javascript", 5)[0]["Link"]) == type("") \
           and type(get_most_voted_results("python", 5)[0]["Votes"]) == type(0)


def test_that_returned_data_is_equal_to_the_number_of_requested_data():
    assert len(get_search_results("how to create a variable", "javascript", 9)) == 9
    assert len(get_most_voted_results("python", 12)) == 12
