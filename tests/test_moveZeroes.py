import pytest
from typing import List
from leetcode.MoveZeroes import Solution


s = Solution()


@pytest.mark.parametrize("nums, answer", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0,1,3,0,0,0,0,3,12,41], [1,3,3,12,41,0,0,0,0,0]),
    ([2,1,0,3,12,0,2], [2,1,3,12,2,0,0]),
])
def test_case(nums: List, answer: List):
    assert s.moveZeroes(nums) == answer
