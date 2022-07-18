from functions.most_frequent_answers import get_frequent


def test_from_1_to_10_freq_answers():
    assert len(get_frequent('html')) == 10
    assert len(get_frequent('python', 10)) == 10
    assert len(get_frequent('python django', 4)) == 4


def test_50_and_greater_then_50_freq_answers():
    assert len(get_frequent('java', 50)) == 50
    assert len(get_frequent('java', 60)) == 50


def test_returning_list():
    assert type(get_frequent('python')) == type([])


def test_that_the_function_returning_data():
    assert get_frequent('javascript')[0]['Title'] is not None
    assert get_frequent('python')[0]['Link'] is not None


