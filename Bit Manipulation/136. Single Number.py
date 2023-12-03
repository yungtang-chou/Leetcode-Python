class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0 ## n ^ 0 = n

        for num in nums:
            res = num ^ res
        
        return res