## Solution w/ Two Pointers
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
            
## Solution w/ Binary Search
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(numbers)): ## O(n)
            val = target - numbers[i]

						## binary search: O(logn)
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = (l+r)//2   ## mid = l + (r-l)//2
                if numbers[mid] == val:
                    return [i+1, mid+1]
                elif numbers[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1