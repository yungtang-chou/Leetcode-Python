class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
            elif n in visit:
                return False
            else:
                continue
    
    def sumOfSquares(self, n):
        
        result = 0
        while n > 0:
            result += (n%10)**2
            n = n //10
        
        return result