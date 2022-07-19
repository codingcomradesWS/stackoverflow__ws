import pytest
from functions.annual_salary_calculator import annual_salary_calculator


def test_annual_salary_calculator():
    actual = annual_salary_calculator()
    expected = [
        ['Germany', 'India', 'France', 'United States of America', 'China', 'Taiwan', 'Russian Federation', 'Poland',
         'Canada', 'Brazil'], [57799, 11434, 42965, 152500, 36408, 57500, 48779, 37840, 84238, 21600]]
    assert actual == expected
