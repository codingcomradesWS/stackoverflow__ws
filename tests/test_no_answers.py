from functions.no_answers import get_questions_with_no_answers


# Dictionary keys are: Title, Link, NumberOfAnswers
# The second parameter in the get_questions_with_no_accepted_answers() represent the number of requested questions
def test_getting_from_10_up_to_50_questions():
    assert len(get_questions_with_no_answers("python", 10)) == 10
    assert len(get_questions_with_no_answers("javascript", 30)) == 30
    assert len(get_questions_with_no_answers("html", 50)) == 50


# maximum number of requests is 50, because we don't want to generate traffic on stack overflow.
def test_getting_max_number_of_allowed_requests():
    assert len(get_questions_with_no_answers("python", 100)) == 50
    assert len(get_questions_with_no_answers("python", 1000)) == 50


def test_that_the_function_returns_a_list():
    assert type(get_questions_with_no_answers("javascript", 5)) == type([])


def test_that_get_questions_with_no_accepted_answers_function_is_returning_data():
    assert get_questions_with_no_answers("javascript", 10)[0]["Title"] is not None
    assert get_questions_with_no_answers("javascript", 10)[0]["Link"] is not None \
           and get_questions_with_no_answers("javascript", 10)[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_questions_with_no_answers("javascript", 10)[0]["NumberOfAnswers"] is not None
