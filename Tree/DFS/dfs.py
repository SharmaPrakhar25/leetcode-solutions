class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversal:
    def __init__(self, root):
        self.root = root
    
    def inorderTraversal(self, root):
        if root is None:
            return None
        
        curr = root
        self.inorderTraversal(curr.left)
        print(curr.data)
        self.inorderTraversal(curr.right)
        return

    def preOrderTraversal(self, root):
        if root is None:
            return None
        
        curr = root
        print(curr.data)
        self.preOrderTraversal(curr.left)
        self.preOrderTraversal(curr.right)
        return

    def postOrderTraversal(self, root):
        if root is None:
            return None
        
        curr = root
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)
        return
        
    
    
    
    
if __name__ == "__main__":
    pass