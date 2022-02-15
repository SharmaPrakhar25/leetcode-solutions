# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        steps = 0
        if N == 1:
            # print(f"I love {'Geeks'} for {'Geeks'}!")
            # print(f"Moving rod {N} from {fromm} to {to}")
            print('move disk {0} from rod {1} to rod {2}'.format(N, fromm, to))
            return 1
            
        steps += self.toh(N - 1, fromm, aux, to)
        print('move disk {0} from rod {1} to rod {2}'.format(N, fromm, to))
        steps += self.toh(N - 1, aux, to, fromm)
        return steps + 1

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends