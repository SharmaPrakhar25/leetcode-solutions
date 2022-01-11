class Solution {
    public int[] sumZero(int n) 
	{
         int[] a = new int[n];
         int p = -(n / 2);
         if(n % 2 == 1)
		 {
        	 for(int i=0; i<a.length; i++)
			 {
        		 a[i] = p;
        		 p += 1;
        	 }
         }
         else
		 {
        	 for(int i=0; i<a.length; i++) 
			 {
        		 a[i] = p;
        		 p += 1;
        		 if(p == 0)
				 {
        			 p ++;
        		 }
        	 }
         }
         return a;
    }
}