# solution
# Runtime: 64 ms, faster than 97.48% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.4 MB, less than 83.97% of Python3 online submissions for Basic Calculator II.

class Solution:
    def calculate(self, s: str) -> int:
        inner, outer, result, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer