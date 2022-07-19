import pytest

from functions.stack_api import *


def test_that_search_and_high_vote_results_are_returned(get_search, get_votes):
    assert get_search[0]["Title"] is not None
    assert get_search[0]["Link"] is not None and get_search[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_votes[0]["Title"] is not None
    assert get_votes[0]["Link"] is not None and get_votes[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_votes[0]["Votes"] is not None


def test_the_returned_data_types(get_search, get_votes):
    assert type(get_search) == type([]) and type(get_votes) == type([])
    assert type(get_search[0]["Title"]) == type("") and type(get_votes[0]["Title"]) == type("")
    assert type(get_search[0]["Link"]) == type("") and type(get_votes[0]["Votes"]) == type(0)


def test_that_returned_data_is_equal_to_the_number_of_requested_data(get_search, get_votes):
    assert len(get_search) == 10
    assert len(get_votes) == 12


@pytest.fixture
def get_search():
    get_search = get_search_results("How to split a list in python", "python", 10, "test_api_search")
    return get_search


@pytest.fixture
def get_votes():
    get_votes = get_most_voted_results("python", 12, "test_api_votes")
    return get_votes
