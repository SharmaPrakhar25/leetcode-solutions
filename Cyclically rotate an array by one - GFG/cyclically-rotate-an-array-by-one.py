#User function Template for python3

def rotate( arr, n):
    tempvalue = arr[-1]
    for idx in range(len(arr)):
        tval = arr[idx]
        arr[idx] = tempvalue
        tempvalue = tval
    
    return arr
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends