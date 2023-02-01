

class Solution():

    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        numbers = []
        for char in s:
            if not numbers:
                numbers.append(romans[char])
                continue
            if romans[char] > numbers[-1]:
                numbers[-1] = romans[char] - numbers[-1]
            else:
                numbers.append(romans[char])
        return sum(numbers)


# s = "MCMXCIV"
s = "MMM"
integer = Solution()
print(integer.romanToInt(s))

