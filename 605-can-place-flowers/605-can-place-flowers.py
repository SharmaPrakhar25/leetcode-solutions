class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < n:
            return False
        
        if len(flowerbed) == 1 and n:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        
        idx = 0
        
        while idx < len(flowerbed) and n>0:
            if flowerbed[idx] != 1:
                if idx == 0: 
                    if flowerbed[idx+1] != 1:
                        n -= 1
                        flowerbed[idx] = 1
                elif idx == len(flowerbed) - 1:
                    if flowerbed[idx-1] != 1:
                        n -= 1
                        flowerbed[idx] = 1
                else:         
                    if flowerbed[idx-1] != 1 and flowerbed[idx+1] != 1:
                        n -= 1
                        flowerbed[idx] = 1  
            idx+=1
        
        return True if n == 0 else False
                
        