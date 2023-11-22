class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ## solution 1
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        
        return False
        
        ## solution 2
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False

        ## solution 3
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False