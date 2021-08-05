# Solution
# Runtime: 32 ms, faster than 63.56% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.1 MB, less than 96.55% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
                "(": ")",
               "[": "]",
               "{": "}"
              }
        stack = []
        
        if len(s) == 0:
            return True
        
        if len(s) % 2 != 0:
            return False
        
        for paren in s:
            if paren in dic:
                stack.append(paren)
            else:
                if len(stack) == 0 or paren != dic[stack.pop()]:
                    return False
        if len(stack) != 0:
            return False
        return True