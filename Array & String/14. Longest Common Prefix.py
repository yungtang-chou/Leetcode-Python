# Solution 1
# Runtime: 28 ms, faster than 94.29% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.4 MB, less than 24.77% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return string[:i]
        
        return strs[0]
    
    
# Solution 2
# Runtime: 32 ms, faster than 82.05% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.5 MB, less than 24.77% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result