def is_armstrong(a):
    # 1^3 + 5^3 + 3^3 = 153
    number = 0
    n = a
    power = 0
    while n > 0:
        n = n//10
        power+= 1
    n = a
    while n > 0:
        temp = n % 10
        number += temp ** power
        n = n//10
    return number == a


if __name__ == '__main__':
    a = int(input())
    print(is_armstrong(a))