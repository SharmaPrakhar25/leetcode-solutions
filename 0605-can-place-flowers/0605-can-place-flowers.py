from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_prev = (i == 0 or flowerbed[i - 1] == 0)
                empty_next = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if empty_prev and empty_next:
                    flowerbed[i] = 1  # Place a flower
                    n -= 1  # Reduce the count of flowers to place
                    
                    if n == 0:  # If no more flowers need to be placed
                        return True
        
        return n == 0  # If we have placed all required flowers
