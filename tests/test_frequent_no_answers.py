from frequent_no_answer import get_frequent_no_answer


def test_frequent_no_answers_one_topic():
    actual = len(get_frequent_no_answer('python'))
    expected = 10
    assert actual <= expected


def test_frequent_no_answers_multi_topics():
    actual = len(get_frequent_no_answer("java react"))
    expected = 20
    assert actual <= expected
