def print_n_times(name, n):
    # base condition
    if n == 0:
        return

    print(f"{name} count {n}")  # 10 to 1 print
    print_n_times(name, n-1)
    # print(f"{name} count {n}") 1 to 10 print
    return


def sum_of_N_numbers(n):
    if n == 0:
        return 0

    return n + sum_of_N_numbers(n-1)


def calculate_factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * calculate_factorial(n-1)


def reverse_array_recursively(arr, idx):
    if idx == len(arr):
        return []

    reversed_array = reverse_array_recursively(arr, idx+1)
    reversed_array.append(arr[idx])
    return reversed_array


def reverseArray(arr, start, end):
    if start > end:
        return

    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start + 1, end - 1)
    return arr


def reverseArrayThirdType(arr, n):
    if n == 0:
        return []

    currentElement = arr[n-1]
    return [currentElement] + reverseArrayThirdType(arr, n-1)


if __name__ == '__main__':
    # print(print_n_times('Prakhar', 10))
    # print(sum_of_N_numbers(10))
    # print(calculate_factorial(5))
    # print(check_pallindrome('ABCBA', 0))
    # print(reverse_array_recursively([1, 2, 3, 4, 5], 0))
    print(reverseArray([1, 2, 3, 4, 5], 0, 4))
