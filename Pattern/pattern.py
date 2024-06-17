
# * Function to print basis n X n start pattern
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=" ")
        print(end='\n')
    return


def pattern2(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print('*', end=" ")
        print(end='\n')
    return


def pattern3(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(j + 1, end=" ")
        print(end='\n')
    return


def pattern4(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(i+1, end=" ")
        print(end='\n')
    return


def pattern5(n):
    for i in range(n):
        for j in range(n):
            if j < n - i:  # 5, 4, 3, 2, 1
                print('*', end=' ')
        print(end='\n')
    return


def pattern6(n):
    for i in range(n):
        for j in range(n):
            if j < n - i:  # 5, 4, 3, 2, 1
                print(j + 1, end=' ')
        print(end='\n')
    return


def pattern7(n):
    for i in range(n):
        # spaces
        for j in range(n-i):
            print("s", end="")

        for k in range(1, 2*i+2):
            print("*", end="")

        # spaces
        for l in range(n-i):
            print("s", end="")

        print(end="\n")


def pattern8(n):
    for i in reversed(range((n))):
        # spaces
        for j in range(n-i):
            print("s", end="")

        for k in range(1, 2*i+2):
            print("*", end="")

        # spaces
        for l in range(n-i):
            print("s", end="")

        print(end="\n")


# print binary of i
def pattern11(n):
    firstValue = 1
    for i in range(n):
        rowValue = firstValue
        for j in range(i+1):
            print(rowValue, end=" ")
            rowValue = 1 - rowValue
        firstValue = 1 - firstValue
        print(end="\n")


def randomPattern(n):
    number = 1
    myList = [[0 for _ in range(n)] for _ in range(n)]
    for col in range(n):
        if col % 2 == 0:
            for row in range(n):
                if row >= col:
                    myList[row][col] = number
                    number += 1

        if col % 2 == 1:
            for row in reversed(range(n)):
                if row >= col:
                    myList[row][col] = number
                    number += 1

    return myList


def pattern19(n):
    for row in range((2*n)-1):
        for col in range((2*n)):
            if row < n:
                if col <= row or col >= ((2*n)-1-row):
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                if col < ((2*n)-1-row) or col > row:
                    print("*", end="")
                else:
                    print(" ", end="")
        print(end="\n")


def pattern13(n):
    number = 1
    for i in range(n):
        for j in range(n):
            if (j <= i):
                print(number, end=" ")
                number += 1
        print(end="\n")


# def pattern19AnotherWay(n):
#     space = 0
#     for i in range((2*n)+1):
#         for j in range(abs(n - i)):
#             print("*", end=" ")

#         for k in range(space):
#             print(" ", end=" ")

#         for l in range(abs(n-i)):
#             print("*", end=" ")

#         if i < n:
#             space += 2
#         else:
#             space -= 2

        # print(end="\n")

def boundaryPattern(n):
    for i in range(n):
        for j in range(n):
            if (i == 0) or (j == 0) or (i == n-1) or (j == n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(end="\n")


def finalPattern(n):
    colToRepeat = (2*n)-1
    for i in range((2*n)-1):
        numberToPrint = n
        repeatCol = colToRepeat
        print(i, repeatCol)
        for j in range((n):
            if j < i:
                numberToPrint = abs(n - j)
                print(numberToPrint, end=" ")
            else:
                if (repeatCol > 0):
                    repeatCol -= 1
                    print(abs(n-i), end=" ")
                else:
                    print(numberToPrint, end=" ")
                    numberToPrint += 1

        if i >= n - 1:
            colToRepeat += 2
        else:
            colToRepeat -= 2

        print(end="\n")


if __name__ == "__main__":
    n = int(input())
    # print(pattern1(n))
    # print(pattern2(n))
    # print(pattern3(n))
    # print(pattern4(n))
    # print(pattern5(n))
    # print(pattern6(n))
    # print(pattern7(n))
    # print(pattern8(n))
    # print(pattern11(n))
    # matrix = randomPattern(n)
    # for row in matrix:
    #     for element in row:
    #         # Adjust the number inside {} to increase space if necessary
    #         print(f"{element:4}", end="")
    #     print()
    # print(pattern19(n))
    # print(pattern13(n))
    # print(pattern19(n))
    # print(boundaryPattern(n))
    print(finalPattern(n))