# Runtime: 80 ms, faster than 40.55% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.6 MB, less than 43.37% of Python3 online submissions for Minimum Size Subarray Sum.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ## edge cases
        if min(nums) > target or sum(nums) < target:
            return 0
        
        ## sliding window method
        total, start = 0, 0
        minLength = math.inf
        
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                ## check the minimum length
                minLength = min(minLength, end - start + 1)
                
                ## start slide to the right 
                total -= nums[start]
                start += 1
        
        if minLength == math.inf:
            return 0
        
        return minLength
        