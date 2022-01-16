class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        mapper = [0] * len(seats) 
        lastFilledIndex = None
        for idx in range(len(seats)):
            if seats[idx] == 1:
                lastFilledIndex = idx
                continue
            else:
                if lastFilledIndex is not None:
                    print(idx)
                    mapper[idx] = abs(lastFilledIndex - idx)
                else:
                    mapper[idx] = len(seats)
                
        
        for idx in reversed(range(len(seats))):
            if seats[idx] == 1:
                lastFilledIndex = idx
                continue
            else:
                mapper[idx] = min(mapper[idx],abs(lastFilledIndex - idx))
            
        return max(mapper)

            