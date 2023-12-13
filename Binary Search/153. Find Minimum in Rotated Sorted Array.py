class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minValue = nums[0] ## randomly initiate the minValue
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                minValue = min(minValue, nums[l])
                break
            
            m = (l + r)//2
            minValue = min(minValue, nums[m])
            if nums[m] >= nums[l]:
                l = m +1
            else:
                r = m - 1
            
        return minValue