# Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = []

        for i, num in enumerate(nums):
            match = target - num
            if match in l:
                return [l.index(match), i]
            else:
                l.append(num)