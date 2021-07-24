# Solution
# Runtime: 208 ms, faster than 90.84% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.5 MB, less than 83.56% of Python3 online submissions for Rotate Array.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## If k > len(nums), we only care about the modular number
        k = k % len(nums)
        
        nums[:k], nums[k:] = nums[-k:], nums[:len(nums)-k]