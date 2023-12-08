## Solution 1:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        answer = [prefix[i] * postfix[i] for i in range(len(nums))]
        
        return answer
    
## Solution 2:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums), 0, -1):
            answer[i-1] *= postfix
            postfix *= nums[i-1]
        
        return answer
