class Solution:
    def reverseArray(self, arr, left, right):
        while left <= right:
            arr[left], arr[right]= arr[right], arr[left]
            left += 1
            right -= 1
        return
    
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for idx in range(len(target)):
            if target[idx] != arr[idx]:
                for j in range(idx, len(arr)):
                    if arr[j] == target[idx]:
                        self.reverseArray(arr, idx, j)
            
        
        return target == arr
             