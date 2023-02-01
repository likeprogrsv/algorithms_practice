import pytest
from typing import List
from leetcode.Two_Sum import Solution


s = Solution()


@pytest.mark.parametrize('list, target, answer', [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([2, 7, 11, 15], 26, [2, 3]),
    ([2, 7, 11, 15], 14, None),
])
def test_two_sum(list: List, target: int, answer: List):
    assert s.two_sum(list, target) == answer
