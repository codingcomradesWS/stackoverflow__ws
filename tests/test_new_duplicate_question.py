import pytest


def test_duplicated_question_case1(list_of_dicts_1):
    actual = list_of_dicts_1[0]["Title"].find("[duplicate]")
    expected = 54
    assert actual == expected


def test_duplicated_question_case2(list_of_dicts_2):
    actual = list_of_dicts_2[0]["Title"].find("[duplicate]")
    expected = -1
    assert actual == expected



@pytest.fixture
def list_of_dicts_1():
    list_1 = [{"Title": "Is grid something defined on the JavaScript language? [duplicate]",
               "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"}]
    return list_1


@pytest.fixture
def list_of_dicts_2():
    list_1 = [{"Title": "Is grid something defined on the JavaScript language?",
               "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"}]
    return list_1
