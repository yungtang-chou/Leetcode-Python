class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) ## placeholder for output
        stack = [] ## store the pair of (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
              stackT, stackInd = stack.pop()
              result[stackInd] = i - stackInd
          
            stack.append((t, i))
        return result