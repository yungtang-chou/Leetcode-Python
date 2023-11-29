# Solution
# Runtime: 11 ms
# Memory Usage: 13.5 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            '(': ')',
            '{': '}',
            '[': ']' 
        }

        stack = [] 

        if len(s) == 0:
            return True

        if len(s) % 2 != 0: ## if odd number, it's not valid
            return False

        for c in s:
            if c in dic:
                stack.append(c)
            elif len(stack) == 0 or c != dic[stack.pop()]:
                return False
            else:
                continue

        if len(stack) == 0:
            return True
        return False