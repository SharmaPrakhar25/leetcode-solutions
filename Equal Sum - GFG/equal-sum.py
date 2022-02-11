#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	# code here
    	psum, ssum = arr[0], arr[n-1]  
    	lidx, ridx = 0, n-1
    	while lidx < ridx:
            if psum == ssum:
                if ridx == lidx + 2:
                    return 'YES'
                ridx-=1
                lidx+=1
                psum += arr[lidx]
                ssum += arr[ridx]
            elif psum > ssum:
                ridx -= 1
                ssum += arr[ridx]
            elif psum < ssum:
                lidx += 1
                psum += arr[lidx]
                
        return 'NO'

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends