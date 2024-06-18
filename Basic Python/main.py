import math

# sample generator code in python
def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k


def displayBasicInfo():
    name = input("Enter your name: ")
    mail = input('Enter your email: ')
    # print('welcome ', name, 'you have provided ', mail, 'this as your email address')
    print(f"Welcome {name}, You have provided {mail} as your email address")


def computeFactorial():
    answer = 1
    number = int(input('Enter the number to find the factorial: '))
    while number > 0:
        answer *= number
        number -= 1
    
    print(answer)


def areaOfCircle():
    radius = float(input("Enter radius of the circle: "))
    pi = math.pi

    print(pi * (radius ** 2))
    

def isPrime():
    number = int(input('Enter the number to check if it is a prime number: '))

    #  logic 1 
    # for num in range(2, number):
    #     if number % num == 0:
    #         print(False)
    #         return
    # print(True)

    # logic 2
    x = math.sqrt(number)
    while x > 1:
        if number % x == 0:
            print(False)
            return
        x -= 1
    
    print(True)


def findGCD():
    # firstNumber = int(input("Enter first number: "))
    # secondNumber = int(input("Enter second number: "))

    numbers = input("Enter numbers with space").split(" ")
    firstNumber = int(numbers[0])
    secondNumber = int(numbers[1])

    minNumber = secondNumber if firstNumber > secondNumber else firstNumber
    while minNumber > 1:
        if firstNumber % minNumber == 0 and secondNumber % minNumber == 0:
            print(minNumber)
            return
        minNumber -= 1
    
    print('There is no common number that divides both the number')
    return


def findGCPAnotherMethod():
    numbers = input("Enter numbers to find GCD: ")
    firstNumber = int(numbers.split(" ")[0])
    secondNumber = int(numbers.split(" ")[1])

    while secondNumber > 0:
        # print(f"First number {firstNumber} secondNumber {secondNumber} and remainder {firstNumber % secondNumber}")
        temp = secondNumber
        secondNumber = firstNumber % secondNumber
        firstNumber = temp
    print(firstNumber)
   
def countVowels():
    count = 0
    str = input("Enter string to: ")
    vowelMap = set(['a','e','i','o', 'u'])
    for idx in range(len(str)):
        if str[idx] in vowelMap:
            count += 1
    
    print(count)

def isMultiple():
    numbers = input("Enter Numbers: ")
    try:
        m = int(numbers.split(" ")[0])
        n = int(numbers.split(" ")[1])
        # this function should verify that n = m * i
        print(n % m == 0)
        # or 
        # for i in range(n):
        #     if m * i == n:
        #         print(True)
        #         return
        # print(False)

    except IndexError:
        print("Error: Not enough values")


def minMax():
    min, max = math.inf, -math.inf
    numbers = [int(x) for x in input("Enter numbers: ").split(" ")]
    for num in numbers:
        if num < min:
            min = num
        
        if num > max:
            max = num

    return (min, max)


def sumOfSquaresLessThanN():
    n = int(input("Enter number: "))
    return sum([i ** 2 for i in range(n)])

if __name__ == "__main__":
    # sample loop to use generators
    # for factor in factors(100):
    #     print(factor)

    # Question1 - Ask user for basic information and display it on terminal
    # displayBasicInfo()

    # Question2 - Calculate factorial for a number
    # computeFactorial()

    # Question3 - Calculate the area of circle
    # areaOfCircle()

    # Question4 - Check if a number is Prime or not
    # isPrime()

    # Questio5 - Find GCP of 2 number
    # findGCD()
    # findGCPAnotherMethod()

    # Question6 - Find the number of vowels in string
    # countVowels()

    # Question7 - Check if n is multiple of m
    # isMultiple()

    # Question8 - Get more than 3 values in input and return minMax in the form of tuple
    # min, max = minMax()
    # print(f"Min of the given number is {min} and Max of the given number is {max}")

    # Question 9 - Return sum of squares of all the numbers less than n and greater than 0
    print(sumOfSquaresLessThanN())


    pass