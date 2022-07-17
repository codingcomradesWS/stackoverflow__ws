from functions.best_companies_hiring import get_best_companies_hiring


def test_python_hiring():
    actual = len(get_best_companies_hiring('python'))
    expected = 10
    assert actual <= expected


def test_random_hiring():
    actual = get_best_companies_hiring('accounting')
    expected = []
    assert actual == expected
