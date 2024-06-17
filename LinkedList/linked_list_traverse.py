def print_pattern_20(n):
    space = 8
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end='')

        for k in range(0, space):
            print(' ', end='')

        for l in range(0, i+1):
            print('*', end='')
        print('\n')
        space -= 2

    space = 0
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print('*', end='')

        for k in range(0, space):
            print(' ', end='')

        for l in range(i, 0, -1):
            print('*', end='')
        print('\n')
        space += 2
    return


def print_pattern_21(n):
    for i in range(0, n):  # 0,1,2,3,4
        for j in range(0, n):  # 0,1,2,3,4
            if i == 0 or i == n-1:
                print(f"{i}{j}", end='')

            if (i > 0 and i < n-1) and (j == 0 or j == n-1):
                print(f"{i}{j}",  end='')
            else:
                print(' ', end='')
        print('\n')


if __name__ == "__main__":
    n = 4
    print_pattern_21(n)
