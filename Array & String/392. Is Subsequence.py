# Solution
# Runtime: 28 ms, faster than 88.82% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.1 MB, less than 98.26% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        i = 0
        for l in t:
            if i < len(s) and l == s[i]:
                i += 1
        
        
        return i == len(s)
        