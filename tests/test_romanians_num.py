import pytest
from .romans_numbers import Solution


integer = Solution()

@pytest.mark.parametrize("str, answer",[
    ("MMM", 3000),
     ("MCMXCIV", 1994)
])
def test_eval(str, answer):
    assert integer.romanToInt(str) == answer

