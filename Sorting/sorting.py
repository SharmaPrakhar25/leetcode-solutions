def selectionSort(arr):
    minIndex = 0
    while minIndex < len(arr):
        tempIndex = minIndex
        for i in range(minIndex+1, len(arr)):
            if arr[i] < arr[tempIndex]:
                tempIndex = i
        arr[minIndex], arr[tempIndex] = arr[tempIndex], arr[minIndex]
        minIndex += 1
    return arr


def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            tempA = j - 1
            if arr[tempA] > arr[j]:
                arr[tempA], arr[j] = arr[j], arr[tempA]

    return arr


def insertionSort(arr):
    return arr


def calculatePower(x, n):
    if n == 0:
        return 1

    return x * calculatePower(x, n-1)


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            print(c, end=" ")
        # return b

def fibbonacciSeriesRecursively(n):
    if n == 0 or n == 1:
        return n
    
    temp = fibbonacciSeriesRecursively(n-2) + fibbonacciSeriesRecursively(n-1)
    print(temp)
    return temp


if __name__ == "__main__":
    # arr = [10, 23, 5, 4, 90]
    print(fibbonacciSeriesRecursively(9))
