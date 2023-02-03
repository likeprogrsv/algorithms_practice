from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            ans[i] = count
        return ans
