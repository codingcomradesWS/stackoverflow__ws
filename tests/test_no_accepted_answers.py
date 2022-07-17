from no_accepted_answers import get_questions_with_no_accepted_answers

def test_no_accepted_answers_one_topic():
    actual = len(get_questions_with_no_accepted_answers('python'))
    expected = 10
    assert actual == expected


def test_no_accepted_answers_multi_topics():
    actual = len(get_questions_with_no_accepted_answers("html css"))
    expected = 10
    assert actual == expected
