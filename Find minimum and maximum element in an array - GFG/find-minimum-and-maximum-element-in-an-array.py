#User function Template for python3

def getMinMax( a, n):
    minNumber = a[0]
    maxNumber = a[0]
    for idx in range(1, len(a)):
        if a[idx] <= minNumber:
            minNumber = a[idx]
        elif a[idx] > maxNumber:
            maxNumber = a[idx]
    return minNumber, maxNumber
            
            
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends