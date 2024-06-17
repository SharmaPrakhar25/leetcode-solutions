# understanding generators
def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k


if __name__ == "__main__":
    for factor in factors(100):
        print(factor)
