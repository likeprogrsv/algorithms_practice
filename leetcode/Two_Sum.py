# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        diction: dict = {x: x for x in nums}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diction and nums.index(diff) != i:
                return [i, nums.index(diff)]


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
