# Solution
# Runtime: 52 ms, faster than 26.21% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.5 MB, less than 26.86% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1