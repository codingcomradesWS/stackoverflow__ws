import time

import pytest
from functions.stack_api import *


def test_that_search_and_high_vote_results_are_returned(get_search_mock, get_votes_mock):
    assert get_search_mock[0]["Title"] is not None
    assert get_search_mock[0]["Link"] is not None and get_search_mock[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_votes_mock[0]["Title"] is not None
    assert get_votes_mock[0]["Link"] is not None and get_votes_mock[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_votes_mock[0]["Votes"] is not None


def test_the_returned_data_types(get_search_mock, get_votes_mock):
    assert type(get_search_mock) == type([]) and type(get_votes_mock) == type([])
    assert type(get_search_mock[0]["Title"]) == type("") and type(get_votes_mock[0]["Title"]) == type("")
    assert type(get_search_mock[0]["Link"]) == type("") and type(get_votes_mock[0]["Votes"]) == type(0)


def test_that_returned_data_is_equal_to_the_number_of_requested_data(get_search_mock, get_votes_mock,
                                                                     get_search_api, get_votes_api):
    assert len(get_search_mock) == 10
    assert len(get_votes_mock) == 12
    assert len(get_search_api) == 1
    assert len(get_votes_api) == 1


def test_getting_max_number_of_allowed_requests(get_search_mock, get_votes_mock):
    assert len(get_search_results("How to split a list in python", "python", 100, "test_api_search")) == 50
    assert len(get_most_voted_results("python", 1000, "test_api_votes")) == 50


@pytest.fixture
def get_search_mock():
    get_search_mock = get_search_results("How to split a list in python", "python", 10, "test_api_search")
    return get_search_mock


@pytest.fixture
def get_votes_mock():
    get_votes_mock = get_most_voted_results("python", 12, "test_api_votes")
    return get_votes_mock


@pytest.fixture
def get_search_api():
    time.sleep(2)
    get_search_api = get_search_results("How to split a list in python", "python", 1)
    return get_search_api


@pytest.fixture
def get_votes_api():
    time.sleep(3)
    get_votes_api = get_most_voted_results("python", 1)
    return get_votes_api
