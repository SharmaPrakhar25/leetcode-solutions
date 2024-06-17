import sys


def find_largest_element_iterative(arr):
    largest_number = arr[0]
    for i in range(1, len(arr)):
        largest_number = max(largest_number, arr[i])
    return largest_number


def find_largest_element_recursive(arr, idx):
    if idx == len(arr):
        return 0

    largest_number = find_largest_element_recursive(arr, idx+1)
    return max(arr[idx], largest_number)


# iterative solution

def find_second_smallest_and_second_largest_number(arr):
    # !small = float('inf')
    # !second_small = float('inf')
    # !large = float('-inf')
    # !second_large = float('-inf')
    largest = arr[0]
    sLargest = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            sLargest = largest
            largest = arr[i]

        if arr[i] > sLargest and arr[i] < largest:
            sLargest = arr[i]

    smallest = arr[0]
    sSmallest = sys.maxsize
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            sSmallest = smallest
            smallest = arr[i]

        if arr[i] < sSmallest and arr[i] > smallest:
            sSmallest = arr[i]

    return sLargest, sSmallest


def is_array_sorted(arr):
    if len(arr) == 0:
        return True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False

    return True


def remove_duplicates_from_sorted_array(arr):
    # ! brute force , space complexity - O(N) and time complexity - O(N)
    # unique_elements_array = [arr[0]]
    # for i in range(1, len(arr)):
    #     if arr[i] != unique_elements_array[-1]:
    #         unique_elements_array.append(arr[i])
    # return unique_elements_array
    # ! Optimized approach time complexity - O(N) and Space complexity - O(1)
    start = 0
    for tail in range(1, len(arr)):
        if arr[start] != arr[tail]:
            start += 1
            arr[start] = arr[tail]
    return arr[0: start+1]


def left_rotate(arr):
    rotating_element = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = rotating_element
    return arr


def rotate_element_by_D_number(arr, d):
    # !brute force, time complexity O(d*N)
    # while d > 0:
    #     left_rotate(arr)
    #     d -= 1
    # return arr
    # ! pythonic solution, time complexity O(N)
    # * basically using 2 for loops,
    # * first one running from d to len(arr) and second one from 0 to d
    return arr[d: len(arr)] + arr[0: d]


def move_zeroes_to_end(arr):
    last_non_zero_index = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != 0:
            last_non_zero_index = i
            break

    start = 0
    while start < last_non_zero_index:
        if arr[start] == 0:
            arr[start], arr[last_non_zero_index] = arr[last_non_zero_index], arr[start]
            last_non_zero_index -= 1
        start += 1

    return arr


def find_union():
    arr1, arr2 = [], []
    i, j = 0, 0  # Pointers
    union = []  # Union list
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
                j += 1

    while i < len(arr1):
        # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


def find_max_consecutive_ones(arr):
    max_count = 0
    temp_count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            temp_count += 1

        if arr[i] != 1:
            max_count = max(temp_count, max_count)
            temp_count = 0

    return max(temp_count, max_count)


def find_longest_subarray_with_sum(arr, k):
    # Input Format: N = 3, k = 5, array[] = {2,3,5}
    if len(arr) == 1:
        if arr[0] == k:
            return 1
        else:
            return 0

    max_length = 0
    start = 0
    end = 0
    temp_sum = 0
    while end < len(arr):
        while start <= end and temp_sum > k:
            temp_sum -= arr[start]
            start += 1

        if temp_sum == k:
            max_length = max(max_length, end - start + 1)

        end += 1
        if end < len(arr):
            temp_sum += arr[end]

    return max_length


if __name__ == "__main__":
    arr = [int(x) for x in input().split(' ')]
    d = int(input())
    # *print(find_largest_element_iterative(arr))
    # *print(type(arr[0]))
    # *print(find_largest_element_recursive(arr, 0))
    # *print(find_second_smallest_and_second_largest_number(arr))
    # *print(is_array_sorted(arr))
    # print(remove_duplicates_from_sorted_array(arr))
    # print(left_rotate(arr))
    # print(rotate_element_by_D_number(arr, d))
    # print(move_zeroes_to_end(arr))
    # print(find_union())
    print(find_max_consecutive_ones(arr))
