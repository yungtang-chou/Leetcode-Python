# Solution
# Runtime: 44 ms, faster than 84.73% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.2 MB, less than 90.36% of Python3 online submissions for Intersection of Two Arrays II.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []
        for i in range(len(nums1)):
            if nums1[i] not in dic:
                dic[nums1[i]] = 1
            else:
                dic[nums1[i]] += 1
        
        for j in range(len(nums2)):
            if nums2[j] in dic and dic[nums2[j]] > 0:
                result.append(nums2[j])
                dic[nums2[j]] -= 1
        
        return result