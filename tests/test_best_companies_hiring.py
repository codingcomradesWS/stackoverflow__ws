
from best_companies_hiring import get_best_companies_hiring


def test_python_hiring():
    actual = get_best_companies_hiring('python')
    expected = ['Deloitte Deutschland',
                'Picnic',
                'Motius GmbH',
                'Baker Hughes',
                'Breuninger GmbH & Co.',
                'ImFusion GmbH',
                'LeoVegas Mobile Gaming Group',
                'ZEISS Group',
                'Copado Strategic Services',
                'Stardog Union']
    assert actual == expected


def test_random_hiring():
    actual = get_best_companies_hiring('accounting')
    expected = []
    assert actual == expected
