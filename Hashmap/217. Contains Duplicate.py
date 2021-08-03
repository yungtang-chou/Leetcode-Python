# Solution #1
# Runtime: 120 ms, faster than 62.96% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 22.1 MB, less than 10.02% of Python3 online submissions for Contains Duplicate.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return True
        
        return False
    
    
# Solution #2
# Runtime: 128 ms, faster than 28.07% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.6 MB, less than 96.70% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False