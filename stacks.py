'''
Stacks support 3 operations
Push (Time Complexity - O(1))
Pop (Time Complexity - O(1))
Peek/Top (Time Complexity - O(1))


Since a dynamic array can satisfy all the operations mentioned above, 
we can create stacks using dynamic array
'''


class Stack:
    stack = []
    size = 0

    def __init__(self, size: int):
        self.size = size

    def push(self, n: int) -> None:
        self.stack.append(n)
        return

    def pop(self) -> None:
        return self.stack.pop()


class DynamicStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = [-1] * self.capacity
        return

    def getSize(self) -> int:
        length = 0
        for num in self.stack:
            if num != -1:
                length += 1
        return length

    def getCapacity(self) -> int:
        return self.capacity
    
    def resize(self) -> None:
        tempStack = [-1] * 2 * self.capacity
        for idx in range(len(self.stack)):
            tempStack[idx] = self.stack[idx]
        self.stack = tempStack
        self.capacity = 2 * self.capacity
        return
    
    def pop(self) -> int:
        lastNonFilledIndex = self.getSize() - 1
        poppedElement = self.stack[lastNonFilledIndex]
        self.stack[lastNonFilledIndex] = -1
        return poppedElement
    
    def push(self,n: int) -> None:
        lastNonFilledIndex = self.getSize()
        if lastNonFilledIndex == self.capacity:
            self.resize()
        
        self.stack[lastNonFilledIndex] = n
        return
    
    def peek(self) -> int:
        lastNonFilledIndex = self.getSize()
        return self.stack[lastNonFilledIndex - 1]
        
        

if __name__ == "__main__":
    pass