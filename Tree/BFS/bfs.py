from collections import queue

def bfs_using_queue(root):
    if root is None:
        return None
    
    q = []
    q.append(root)
    
    while len(q) > 0:
        curr = q.pop(0)
        print(curr.data)
        
        if curr.left is not None:
            q.append(curr.left)
        
        if curr.right is not None:
            q.append(curr.right)
    
    return