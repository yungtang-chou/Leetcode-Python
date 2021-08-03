# Solution
# Runtime: 40 ms, faster than 81.64% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 96.64% of Python3 online submissions for Isomorphic Strings.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        def checkIso(s, t):
            dic = {}
            for i in range(len(s)):
                if s[i] not in dic:
                    dic[s[i]] = t[i]
                else:
                    if dic[s[i]] != t[i]:
                        return False
            return True
        
        return checkIso(s,t) and checkIso(t,s)