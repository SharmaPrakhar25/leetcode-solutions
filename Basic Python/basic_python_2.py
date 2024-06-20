import random

# * Find the distinct pair of consecutive numbers who product is even from the sequence of numbers
def isProductEven():
    list = [int(x) for x in input("Enter the numbers from sequence").split(" ")]
    # ! Using while loop 
    # a = list[0]
    # idx = 1
    # while idx < len(list):
    #     if list[idx] != a:
    #         if (list[idx] * a) % 2 ==0:
    #             return True
    #     a = list[idx]
    #     idx += 1

    # * Using for loop
    for i in range(len(list)-1): # * we will loop till the second last argument to avoid index out of bound error
        if list[i] != list[i+1]:
            if (list[i] * list[i+1]) % 2 == 0:
                return True
    return False


def reverseAList():
    list = [int(x) for x in input("Enter the numbers for list: ").split()]
    n = len(list)
    for i in range(n//2):
        list[i], list[n-i-1] = list[n-i-1], list[i]
    return list


def generateCharList():
    charList = [chr(x) for x in range(97, 123)]
    print(charList)


def shuffleList():
    list = [int(x) for x in input("Enter numbers to shuffle: ").split(" ")]
    n = len(list)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        list[i], list[j] = list[j], list[i]
    return list

def randomChoice():
    list = [int(x) for x in input("Enter numbers: ").split(" ")]
    n = len(list)
    randomIndex = random.randrange(0, n)
    return list[randomIndex]

# Sample python programme to take continous input from terminal until user click ctrl + d or type exit and print in reverse order
def continousInput():
    inputs = []
    while True:
        try:
            user_input = input("Enter something (type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the loop.")
                break
            inputs.append(user_input)
        except EOFError:
            print("\n Exiting the input loop.")
            break

    print("You entered:", [inputs[s] for s in range(len(inputs)-1, -1, -1)])


def removePunctuationFromString():
    punctuation = set([
    ',',
    ';',
    ':',
    '!',
    '?',
    "'",
    '"',
    '-',
    '(',
    ')',
    '[',
    ']',
    '{',
    '}',
    '...',
    '&',
    '%',
    '/',
    '\\',
    '+',
    '=',
    '_',
    '*',
    '#',
    '@',
    '$',
    '^',
    '~',
    '|',
    '<',
    '>',
    '`',
    '.',
    "'"
    ])
    sampleString = input()
    outputList = []
    for i in range(len(sampleString)):
        ch = sampleString[i]
        if ch in punctuation:
            outputList.append('')
        else:
            outputList.append(ch)

    return ''.join(outputList)


chars = ['c','a','t','d','o','g']
count = 0
def helper(chars, currentString, used=set()):
    global count
    if len(currentString) == len(chars):
        count += 1
        print(count, currentString)
        return
    
    for char in chars:
        if char not in used:
            used.add(char)
            helper(chars, currentString + char, used)
            used.remove(char)


def generatePossibleStringUsingChars():
    return helper(chars, '')


if __name__ == "__main__":
    # reversedList = reverseAList()
    # isProdEven = isProductEven()
    # print(generateCharList())
    # print(shuffleList())
    # print(randomChoice())
    # continousInput()
    # print(removePunctuationFromString())
    print(generatePossibleStringUsingChars())
    pass