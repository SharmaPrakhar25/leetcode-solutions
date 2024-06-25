class Solution:
    def calculateHourHelper(self, arr, k):
        h = 0
        for num in arr:
            h += math.ceil(num / k)

        return h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananaPiles = piles
        bananaPiles.sort()
        start = 1
        end = bananaPiles[-1]
        k = math.inf 
        while start <= end:
            tempk= start + ((end - start)//2)
            tempH = self.calculateHourHelper(bananaPiles, tempk)
            if tempH > h:
                start = tempk + 1

            if tempH <= h:
                k = min(tempk, k)
                end = tempk - 1

        return k
        