# Solution
# Runtime: 44 ms, faster than 79.99% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 37.18% of Python3 online submissions for Valid Anagram.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in dic:
                return False
            else:
                dic[t[j]] -= 1
        
        for k in dic:
            if dic[k] != 0:
                return False
        
        return True
    
    
# Solution
# Runtime: 48 ms, faster than 69.62% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 12.19% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)