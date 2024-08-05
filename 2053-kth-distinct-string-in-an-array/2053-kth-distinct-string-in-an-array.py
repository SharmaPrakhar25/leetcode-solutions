from collections import Counter
from typing import List

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
    
    def __eq__(self, other):
        return self.val == other.val
    
    def __hash__(self):
        return hash(self.val)

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count the occurrences of each string in the array
        counts = Counter(arr)
        
        # List to store distinct nodes (strings that appear exactly once)
        distinct_nodes = []

        # Traverse the array and collect distinct elements
        for idx, s in enumerate(arr):
            if counts[s] == 1:
                distinct_nodes.append(Node(s, idx))
        
        # If there are enough distinct elements, return the k-th one
        if len(distinct_nodes) >= k:
            return distinct_nodes[k-1].val
        
        # If there are not enough distinct elements, return an empty string
        return ""
