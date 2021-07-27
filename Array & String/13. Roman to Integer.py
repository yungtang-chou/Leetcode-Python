# Solution
# Runtime: 48 ms, faster than 67.43% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.3 MB, less than 58.22% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        result = 0
        
        for i in range(len(s)):
            if i > 0 and values[s[i]] > values[s[i-1]]:
                result -= 2 * values[s[i-1]]
                result += values[s[i]]
            else:
                result += values[s[i]]
        return result
        