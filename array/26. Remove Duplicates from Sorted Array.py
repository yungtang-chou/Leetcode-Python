# Solution 1.
# Runtime: 84 ms, faster than 73.56% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.6 MB, less than 73.07% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: ## return 0 if there's no element
            return 0
        
        ## Initialize loc
        loc = 0 
        for i in range(len(nums)):
            if nums[loc] != nums[i]:
                loc += 1
                nums[loc] = nums[i]
        return loc + 1