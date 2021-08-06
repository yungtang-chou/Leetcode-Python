# Solution
# Runtime: 1320 ms, faster than 24.95% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 26.9 MB, less than 5.16% of Python3 online submissions for Maximum Average Subarray I.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = 0 
        maximum = float('-inf')

        if len(nums) == 0:
            return 0
        
        for i, x in enumerate(nums):
            tmp += x
            if i >= k:
                tmp -= nums[i-k]
            
            if i >= k-1:
                maximum = max(maximum, tmp)
        
        return maximum / k