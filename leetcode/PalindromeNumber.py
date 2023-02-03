class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new = 0
        origin = x
        while x:
            x, d = divmod(x, 10)
            new = new * 10 + d

        return new == origin


s = Solution()
print(s.isPalindrome(121))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#        return str(x) == str(x)[::-1]