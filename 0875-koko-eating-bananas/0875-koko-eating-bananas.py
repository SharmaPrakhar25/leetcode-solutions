class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        k = end
        while start <= end:
            tempk = start + ((end - start)//2)
            tempH = 0
            for b in piles:
                tempH += math.ceil(b / tempk)
                
            if tempH > h:
                start = tempk + 1

            if tempH <= h:
                k = min(tempk, k)
                end = tempk - 1

        return k
        