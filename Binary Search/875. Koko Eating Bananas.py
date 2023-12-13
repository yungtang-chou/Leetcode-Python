class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        minValue = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                minValue = min(k, minValue)
                r = k - 1
            else:
                l = k + 1 ## rate is too slow thus we cannot finish it in time
            

        return  minValue