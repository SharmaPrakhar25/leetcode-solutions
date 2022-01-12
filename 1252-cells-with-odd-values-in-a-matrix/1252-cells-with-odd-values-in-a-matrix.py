class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        totalodd = 0
        ansmatrix = [[0 for col in range(n)]for row in range(m)]
        for idx in indices:
            # col = 0
            # row = 0
            
            for col in range(n):
                ansmatrix[idx[0]][col] += 1
                if ansmatrix[idx[0]][col]%2 != 0:
                    totalodd += 1
                else:
                    totalodd -= 1
                    
            # while col < n:
            #     ansmatrix[idx[0]][col] += 1
            #     if ansmatrix[idx[0]][col]%2 != 0:
            #         totalodd += 1
            #     else:
            #         totalodd -= 1
            #     col += 1
            
            for row in range(m):
                ansmatrix[row][idx[1]] += 1
                if ansmatrix[row][idx[1]]%2 != 0:
                    totalodd += 1
                else:
                    totalodd -= 1
                    
            # while row < m:
            #     ansmatrix[row][idx[1]] += 1
            #     if ansmatrix[row][idx[1]]%2 != 0:
            #         totalodd += 1
            #     else:
            #         totalodd -= 1
            #     row += 1
        
        
        # for row in range(m):
        #     for col in range(n):
        #         if ansmatrix[row][col] % 2 == 1:
        #             totalodd += 1
        return totalodd