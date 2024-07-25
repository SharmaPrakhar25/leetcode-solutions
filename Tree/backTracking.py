class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        self.root = Node(val)
        return 

    def backTrack(self, root):
        if root is None or root.data == 0:
            return False 
    
    # leaf node means successfull traverse
        if not root.left and not root.right:
            return True
        curr = root
        if self.backTrack(curr.left):
            return True
        if self.backTrack(curr.right):
            return True 
        return False

if __name__ == "__main__":
    myTree = Tree()
    pass