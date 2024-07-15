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


if __name__ == "__main__":
    pass