class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        halt = 0 
        talt = 0
        for number in gain:
            talt += number
            if talt > halt:
                halt = talt
                
        return halt
        