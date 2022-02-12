#User function Template for python3

class Solution:
   def subArrayExists(self,arr,n):
       s = set([])
       prefix_sum = 0
       for i in range(n):
           prefix_sum += arr[i]
           if prefix_sum in s:
               return True
           if prefix_sum == 0:
               return True
           s.add(prefix_sum)
       return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends