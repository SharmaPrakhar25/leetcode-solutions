def getPivot(arr, low, high):
    left = low
    right = high
    pivot = arr[low]

    while left < right:
        while arr[left] <= pivot and left <= high - 1:
            left += 1

        while arr[right] > pivot and right >= low + 1:
            right -= 1

        if (left < right):
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quickSort(arr, low, high):
    if low > high:
        return

    pivot = getPivot(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)
    return


if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
