
# * lower bound of x is the index after which all the numbers in the array are greater than or equal to x
# * brute force for lower bound, considering array is sorted
# ans = len(arr)
# for i in range(0, len(arr)):
#     if arr[i] == x:
#         ans = i
#         break
# return ans + 1

def find_lower_bound(arr, x):
    # ! we are considering that element is not present in the array because if there is a smaller element than target is
    ans = len(arr)
    # ! present in the array it will be found automatically
    start = 0
    end = len(arr) - 1
    # * incorrect answer, need to solve again
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] >= x:
            ans = mid  # * may be this is my possible answer
            end = mid - 1  # * but I should look a little into left side, because I need smallest index after which >= target

        if arr[mid] < x:
            start = mid + 1

    return ans


def find_upper_bound(arr, x):
    ans = len(arr)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + ((end-start)//2)
        if arr[mid] <= x:
            start = mid + 1

        if arr[mid] > x:
            ans = mid
            end = mid - 1
    return ans


def fandL_index_X(nums, target):
    fIndex, lIndex = -1, -1
    start = 0
    end = len(nums) - 1
    # * I will do first binary search for first Index
    while start <= end:
        mid = start + ((end - start)//2)
        if nums[mid] > target:
            end = mid - 1

        if nums[mid] < target:
            start = mid + 1

        if nums[mid] == target:
            fIndex = mid
            end = mid - 1

    if fIndex != -1:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start)//2)
            if nums[mid] > target:
                end = mid - 1

            if nums[mid] < target:
                start = mid + 1

            if nums[mid] == target:
                lIndex = mid
                start = mid + 1

    return fIndex, lIndex


def count_occurance(nums, target):
    # lowerBound = find_lower_bound(nums, target)
    # if lowerBound < len(nums):
    #     upperBound = find_upper_bound(nums, target)
    #     return upperBound - lowerBound
    fIndex, lIndex = fandL_index_X(nums, target)
    if fIndex > 0:
        return lIndex - fIndex + 1
    return 0


if __name__ == "__main__":
    arr = [int(x) for x in input().split(' ')]
    d = int(input())
    # print(find_lower_bound(arr, d))
    # print(find_upper_bound(arr, d))
    print(count_occurance(arr, d))
