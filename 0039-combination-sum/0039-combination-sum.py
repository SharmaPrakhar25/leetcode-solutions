class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        def helper(start, curTarget, path):
            if start >= len(candidates):
                return
        
            if curTarget < 0:
                return

            if curTarget == 0:
                res.append(path[:])
                return
            
            path.append(candidates[start])
            helper(start, curTarget - candidates[start], path)
            path.pop()
            helper(start+1, curTarget, path)
        
        helper(0, target, path)
        return res
        