# Solution
# Runtime: 44 ms, faster than 78.24% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.3 MB, less than 74.65% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
    
    
# Solution
