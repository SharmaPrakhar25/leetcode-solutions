def findMaxInSubArray(nums, w):
    result = []
    processedElements = []

    for i in range(w):
        """
        Process the first window such that, at the end of the iteration, 
        the elements of the first window are present in your collection in descending order.
        - the hurdle in using the LIST/ARRAY for processed elements 
        is sorting it at each step is an expensive solution
        o(nlogn)
        """
        """
        Using a DEQUEUE is an optimal solution
        because we can delete from both ends 
        """
    pass


if __name__ == "__main__":
    print(findMaxInSubArray([-2, 4, -3, 5, 8], 3))
