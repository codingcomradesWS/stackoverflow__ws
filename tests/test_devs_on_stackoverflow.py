from functions.devs_on_stackoverflow import get_developers_on_stackoverflow


def test_developers_percentage_data():
    assert get_developers_on_stackoverflow()[0]['percentage'] == ' 47% '
    assert get_developers_on_stackoverflow()[0]['type of developers'] == ' consider themselves full-stack developers '


def test_devOps_percentage_data():
    assert get_developers_on_stackoverflow()[1]['percentage'] == ' 10% '
    assert get_developers_on_stackoverflow()[1]['type of developers'] == ' consider themselves DevOps specialists '


def test_returning_list():
    assert type(get_developers_on_stackoverflow()) == type([])


def test_that_the_function_returning_data():
    assert get_developers_on_stackoverflow()[0]['percentage'] is not None
    assert get_developers_on_stackoverflow()[0]['type of developers'] is not None
