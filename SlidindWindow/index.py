'''
Q: Given an array, return true if there are two elements within a window of size k that are equal.
Arr = [1,2,3,2,3,3], k = 3
'''
from typing import List

def equalElementsInWindowK(arr: List[int], k: int):
    '''
    answer with O(n^2) Time Complexity
    '''
    # for i in range(len(arr)):
    #     for j in range(i+1, min(i+k, len(arr))):
    #         if arr[i] == arr[j]:
    #             return True

    # left = 0
    # right = 0
    # windowSet = set([])
    # while right < len(arr):
    #     if right - left + 1 <= k:
    #         if arr[right] in check:
    #             return True
    #         else:
    #             windowSet.add(arr[right])
    #         right += 1
    #     else:
    #         windowSet.remove(arr[left])
    #         left += 1
    
    
    window_start = 0
    seen_numers = set()
    
    for window_end in range(len(arr)):
        if window_end - window_start + 1 > k:
            seen_numers.remove(arr[window_start])
            window_start += 1
        
        if arr[window_end] in seen_numbers:
            return True

        seen_numbers.add(arr[window_end])
            

    return False


def subArrayWithThresoldAverage(arr, k, threshold):
    # brute force
    count = 0
    # for window_start in range(0, len(arr) - k + 1):
    #     curr_sum = 0
    #     for window_end in range(window_start, window_start + k):
    #         curr_sum += arr[window_end]
        
    #     if curr_sum // k >= threshold:
    #         count += 1

    window_start = 0
    curr_sum = 0
    for window_end in range(0, len(arr)):
        if window_end - window_start + 1 > k:
            curr_sum -= arr[window_start]
            window_start += 1
        
        
        curr_sum += arr[window_end]
        
        if window_end - window_start + 1 == k and curr_sum // k >= threshold:
            count += 1
    
    return count
            