class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None
        

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        
        while count < index and curr:
            curr = curr.next
            count += 1
        
        return curr.data if curr else -1 
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        return
            

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        count = 0
        newNode = Node(val)
        while count < index and curr:
            curr = curr.next
            count += 1
        
        if curr:
            if curr == self.head:
                self.addAtHead(val)
                return
            else:
                newNode.next = curr
                newNode.prev = curr.prev
                if curr.prev:
                    curr.prev.next = newNode
                curr.prev = newNode
        else:
            if count == index:
                self.addAtTail(val)
            return
        return
            
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        
        while count < index and curr:
            curr = curr.next
            count += 1
        
        if curr:
            if curr == self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None 
            elif curr == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
        return
    
    def lengthOfLinkedList(self) -> int:
        curr = self.head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        
        return count
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)