import pytest

from .balanced_symbols_string import is_balanced


@pytest.mark.parametrize(
    "symbols, expected_response",
    (
        ("({[]})", True),
        ("(({[]}))", True),
        ("(([{{}}]))", True),
        ("(([{{}}])", False),
        ("(}([{{}}]))", False),
        ("(({[]})", False),
    ),
)
def test_is_balanced(symbols, expected_response):
    assert is_balanced(symbols) is expected_response
