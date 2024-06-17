
def merge(arr, start, mid, end):
    temp = []
    left = start
    right = mid+1

    while left <= mid and right <= end:
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= end:
        temp.append(arr[right])
        right += 1

    for i in range(start, end+1):
        arr[i] = temp[i - start]

    return


def mergeSort(arr, start, end):
    if (start >= end):
        return

    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    merge(arr, start, mid, end)

    return arr


if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    mergeSort(arr, 0, len(arr)-1)
