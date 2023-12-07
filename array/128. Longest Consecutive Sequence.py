## Solution w/ Sets
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        sets = set(nums)
        maxLength = 0

        for num in nums:
            ## check if its the start of a sequence
            if (num - 1) not in sets:
                length = 0
                while (num + length) in sets:
                    length += 1
                
                maxLength = max(length, maxLength)
        
        return maxLength
    

## Solution w/ Sort
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0

        nums.sort()
        maxLength = 0
        currLength = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                currLength += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                maxLength = max(maxLength, currLength)
                currLength = 1
        
        maxLength = max(maxLength, currLength)
        
        return maxLength