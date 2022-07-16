from functions.newest_questions import get_recent_questions


# Dictionary keys are: Title, Link, Date&Time
# The second parameter in the get_recent_questions() represent the number of requested questions
def test_getting_from_10_up_to_50_questions():
    assert len(get_recent_questions("python", 10)) == 10
    assert len(get_recent_questions("python", 30)) == 30
    assert len(get_recent_questions("python", 50)) == 50


# maximum number of requests is 50, because we don't want to generate traffic on stack overflow.
def test_getting_max_number_of_allowed_requests():
    assert len(get_recent_questions("python", 100)) == 50
    assert len(get_recent_questions("python", 1000)) == 50


def test_that_the_function_returns_a_list():
    assert type(get_recent_questions("javascript", 5)) == type([])


def test_that_get_recent_questions_function_is_returning_data():
    assert get_recent_questions("javascript", 10)[0]["Title"] is not None
    assert get_recent_questions("javascript", 10)[0]["Link"] is not None \
           and get_recent_questions("javascript", 10)[0]["Link"].startswith('https://stackoverflow.com/questions')
    assert get_recent_questions("javascript", 10)[0]["Date&Time"] is not None
