# Solution
# Runtime: 64 ms, faster than 65.85% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.8 MB, less than 32.32% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers) -1
        sum = 0
        
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return start +1, end+1