class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n /= 2
            else:
                count += (n-1)//2
                n = (n-1)/2 + 1
        
        return count
    
## simpler solution
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        while n > 1:
            count += n // 2
            n -= n // 2
        
        return count