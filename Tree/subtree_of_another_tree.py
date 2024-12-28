class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
'''
Another implementation of the solution
def is_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.data == tree2.data and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right))

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    if not root:
        return False
    return is_same_tree(root, sub_root) or subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)

'''
        
def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    # Base case
    if root is None and sub_root is None:
        return True
    
    # If one of the trees is empty and the other is not, they are not the same
    '''
        if root is not None and sub_root is None:
            return False
        
        if root is None and sub_root is not None:
            return False
            
        This could also be return as 
        if (root is not None) or (sub_root is not None):
            return False
    '''
    if (root is None) != (sub_root is None):
        return False
    
    if root.data == sub_root.data:
        return subtree_of_another_tree(root.left, sub_root.left) and subtree_of_another_tree(root.right, sub_root.right)
    else:
        return subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)
        

def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    sub_root = build_tree(iter(input().split()), int)
    res = subtree_of_another_tree(root, sub_root)
    print("true" if res else "false")