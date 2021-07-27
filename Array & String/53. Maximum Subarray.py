# Solution
# Runtime: 56 ms, faster than 97.78% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.9 MB, less than 85.06% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        local_max, global_max = 0, 0
        
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        
        return global_max