## Solution 1: Heap
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ## step 1: get counts for each element using hashmap
        count = dict()

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        ## step 2: use min-heap to store top k frequent elements
        heap = []
        for num, count in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        
        ## step 3: return the elements from the heap
        return [num for count, num in heap]
        

## Solution 2: Array + Hashmap
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ## hashmap to count occurrences
        count = dict()

        ## table to store occurrences vs values
        ## the max occurence is the length of input array
        freq = [[] for i in range(len(nums) + 1)]

        ## update counts
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        ## get result
        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result