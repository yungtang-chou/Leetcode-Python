# Solution
# Runtime: 28 ms, faster than 82.20% of Python3 online submissions for Word Pattern.
# Memory Usage: 14.1 MB, less than 93.22% of Python3 online submissions for Word Pattern.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l_pattern = list(pattern)
        l_s = s.split(' ')
        if len(l_pattern) != len(l_s):
            return False
        
        def compare(l_pattern, l_s):
            dic = {}
            for i in range(len(l_pattern)):
                if l_pattern[i] not in dic:
                    dic[l_pattern[i]] = l_s[i]
                else:
                    if dic[l_pattern[i]] != l_s[i]:
                        return False
            return True
    
        return compare(l_pattern, l_s) and compare(l_s, l_pattern)
    
