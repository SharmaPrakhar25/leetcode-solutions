from typing import List
'''
Q. How does python handles the reference to the object 
A. In hindsight python uses pointers but in a more abstracted way, so when we create a variable, the variable name holds the reference to the object
a = [1, 2, 3]
b = a  # b now references the same list object as a
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3]
a.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]  # b sees the change because it references the same object
a and b both reference the same list object.

1. In python variables do not directly store the value of an object.
2. Python uses a combination of reference counting (number of variables referencing to the object) and garbage collection to manage memory (Garbage collection is used to detect and clean up cycles of references that cannot be handled by reference counting alone.)
3. Problem with Reference Counting: Cyclic References
However, reference counting has a limitation: it cannot handle cyclic references.
A cyclic reference occurs when two or more objects reference each other, creating a cycle. 
Since their reference counts never drop to zero, they are never freed, leading to a memory leak.

Garbage Collection: Detecting and Cleaning Up Cycles
To address this issue, Python uses a cyclic garbage collector in addition to reference counting. The cyclic garbage collector is part of the gc module and works as follows:

Tracking Objects:

The garbage collector periodically scans objects in memory to track references and identify potential cycles.
Detecting Cycles:

It builds a reference graph to detect groups of objects that reference each other but are not reachable from the root (i.e., they form isolated cycles).
Breaking Cycles:

Once a cycle is detected, the garbage collector breaks the cycle by decreferring references, allowing the reference counts to drop to zero and freeing the memory occupied by these objects.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        current = self.head
        while index > 0 and current:
            current = current.next
            index -= 1
        return current.data if current  else -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
            # self.head.next = self.tail
        else:
            node.next = self.head
            self.head = node
        return

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        prev = None
        curr = self.head
        count = 0

        while count < index and curr is not None:
            prev = curr
            curr = curr.next
            count +=1 
        
        if not curr:
            return False
        
        if not prev:
            self.head = curr.next
        else:
            prev.next = curr.next
        
        if curr == self.tail:
            self.tail = prev

        return True

    def getValues(self) -> List[int]:
        linked_list = []
        currentNode = self.head
        while currentNode is not None:
            linked_list.append(currentNode.data)
            currentNode = currentNode.next
        return linked_list       

    '''
    def reverseALinkedList(self) -> Node
    If you want to return the head of reversed linked list
    use Node in return
    '''
    def reverseALinkedList(self) -> None:
        prev = None
        curr = self.head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        
        self.head = prev
        return



if __name__ == "__main__":
    my_ll = LinkedList()
    print(my_ll.insertHead(1))
    # my_ll.insertTail(2)
    # my_ll.insertHead(2)
    print(my_ll.remove(0))
    # print(my_ll.getValues())
    # print(my_ll.get(5))

    