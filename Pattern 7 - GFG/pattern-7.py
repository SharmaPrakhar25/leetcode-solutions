#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for k in range(N-1, i-1, -1):
                # print(k)
                print(' ', end='')
            
            for j in range(0, 2*i-1):
                print('*', end="")
            
            print(end='\n')
        return


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends