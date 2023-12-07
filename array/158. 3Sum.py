class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ## two sum with dynamic target value
        result = []
        nums.sort()

        for i in range(len(nums)-2):

            ## avoid duplicates for the first value
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    # avoid duplicates for the second value
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            
        return result