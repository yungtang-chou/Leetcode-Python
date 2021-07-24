# Solution 1
# Runtime: 36 ms, faster than 40.87% of Python3 online submissions for Remove Element.
# Memory Usage: 14.1 MB, less than 73.71% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start] ## swap
                end -= 1
            else:
                start += 1
        return start


# Solution 2

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)