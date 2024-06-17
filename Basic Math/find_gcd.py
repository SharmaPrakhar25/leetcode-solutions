def find_gcd(a,b):
    gcd = 1
    # if we reduce the range to the min of a and b, we can reduce the loop number of execution
    # because number greater the number given in input, can not divide the number in input so it will not
    # example in case of 8 and 12 --> 9,10,11 can not divide 8 so there's no point in checking that 
    for i in range(2, min(a,b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def find_gcd_recursively(a, b):
    if b == 0:
        return a
    # so there's a thing called Euclidean Algorithm, which says that if there's a number X
    # which is the GCD(A,B) == X, then X should also be the GCD OF GCD(B, A%B)
    return find_gcd_recursively(b, a%b)



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(find_gcd(a, b))
    print(find_gcd_recursively(a,b))