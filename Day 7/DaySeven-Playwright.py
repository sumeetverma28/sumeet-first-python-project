"""Pytest HTML report example.

Run the following command to generate a self-contained HTML report:
    pytest --html=reports/report.html --self-contained-html
"""


def test_addition():
    assert 2 + 2 == 4


def test_string_contains_pytest():
    assert "pytest" in "pytest-html"
