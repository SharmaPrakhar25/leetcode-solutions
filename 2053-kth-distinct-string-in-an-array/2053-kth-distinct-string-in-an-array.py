class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count the occurrences of each string in the array
        counts = Counter(arr)
        # List to store distinct nodes (strings that appear exactly once)
        distinct_nodes = [s for s in arr if counts[s] == 1]
        # If there are enough distinct elements, return the k-th one
        if len(distinct_nodes) >= k:
            return distinct_nodes[k-1]
        # If there are not enough distinct elements, return an empty string
        return ""
