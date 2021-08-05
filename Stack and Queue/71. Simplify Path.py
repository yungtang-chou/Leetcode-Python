# Solution
# Runtime: 24 ms, faster than 97.48% of Python3 online submissions for Simplify Path.
# Memory Usage: 14.3 MB, less than 72.13% of Python3 online submissions for Simplify Path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        for i in path.split('/'):
            if i == '.':
                continue
            elif i == '..' and len(stack) > 0:
                stack.pop()
            elif i == '..' and len(stack) == 0:
                continue
            elif i == '':
                continue
            else:
                stack.append(i)
        
        return '/' + '/'.join(stack)