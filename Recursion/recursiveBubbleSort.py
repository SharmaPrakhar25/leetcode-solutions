def rbs(arr, idx):
    # print(arr, idx)
    if idx == 0:
        return

    if (arr[idx] < arr[idx-1]):
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx]

    rbs(arr, idx-1)


def rbss(arr, idx):
    if idx == 1:
        return

    for j in range(0, idx-1):
        if (arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

    rbss(arr, idx-1)


if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    rbss(arr, len(arr))
    print('final answer')
    print(arr)
