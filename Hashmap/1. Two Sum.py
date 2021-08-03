## Solution #1
# Runtime: 1016 ms, faster than 31.91% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 80.47% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                return nums.index(i), next_index + temp_nums.index(j)

## Solution #2
# Runtime: 60 ms, faster than 76.60% of Python3 online submissions for Two Sum.
# Memory Usage: 15.4 MB, less than 20.39% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]], i]