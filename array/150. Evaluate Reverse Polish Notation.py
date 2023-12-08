class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        operands = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    res = int(num2) + int(num1)
                elif token == '-':
                    res = int(num2) - int(num1)
                elif token == '*':
                    res = int(num2) * int(num1)
                else:
                    res = int(float(num2) / int(num1))
                stack.append(res)
        return stack[0]