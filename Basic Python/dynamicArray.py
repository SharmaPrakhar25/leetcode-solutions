class DynamicArray:
    array = []
    capacity = 0
    size = 0

    def __init__(self, capacity: int):
        self.array = [-1] * capacity 
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        return 

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        tempArray = [-1] * self.capacity
        for i in range(self.size):
            tempArray[i] =  self.array[i] 
        self.array = tempArray
        return

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity

    def printArray(self) -> None:
        for num in self.array:
            print(num, end=' ')
        return

if __name__ == "__main__":
    array1 = DynamicArray(1)
    # array1.pushback(1)
    print('Size', array1.getSize())
    print('Capacity', array1.getCapacity())
    print('pushing element',array1.pushback(1))
    print('Size', array1.getSize())
    print('Capacity',array1.getCapacity())
    print('pushing element',array1.pushback(2))
    print('Size', array1.getSize())
    print('Capacity', array1.getCapacity())
    print(array1.printArray())
    print('GET', array1.get(1))
    array1.set(1,3)
    print('GET', array1.get(1))
    print('Popback', array1.popback())
    print('Size', array1.getSize())
    print('Capacity', array1.getCapacity())

    
    
