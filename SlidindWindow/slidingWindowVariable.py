def longestSubArrayWithSameValue(arr):
    res = 0
    
    # for window_start in range(len(arr)):
    #     window_end = window_start + 1
    #     tempMax = 1
    #     while window_end < len(arr):
    #         if arr[window_start] == arr[window_end]:
    #             tempMax += 1
    #             window_end += 1
    #         else:
    #             res = max(res, tempMax)
    #             break
    
    window_start = 0
    for window_end in range(len(arr)):
        if arr[window_end] != arr[window_start]:
            window_start = window_end
        
        res = max(res, window_end - window_start + 1)
    return res
                
            