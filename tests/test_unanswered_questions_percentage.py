import pytest
from functions.unanswerd_questions_percentage import unanswered_questions_percentage


def test_returned_list_length(dict_list):
    actual = len(dict_list)
    expected = 10
    assert actual == expected


def test_dict_keys(dict_list):
    actual = list(dict_list[0].keys())
    expected = ['tag', 'unanswered_7days', 'unanswered_30days', 'unanswered_all_time']
    assert actual == expected


@pytest.fixture
def dict_list():
    return unanswered_questions_percentage()


