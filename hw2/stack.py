class Stack:
    def __init__(self, max_size: int = float("inf")) -> None:
        self.__max_size = max_size
        self.__arr = []
        self.__top = -1

    def push(self, value: any) -> None:
        if self.isFull():
            raise Exception("Stack is full, you can not push!")

        self.__arr.append(value)
        self.__top += 1
    
    def pop(self) -> any:
        if self.isEmpty():
            raise Exception("Stack is empty, you can not pop!")
        
        self.__top -= 1
        return self.__arr.pop()
    
    def peek(self) -> any:
        if not self.isEmpty():
            return self.__arr[-1]
        return None
    
    def isFull(self) -> bool:
        return self.__top >= self.__max_size - 1
    
    def isEmpty(self) -> bool:
        return self.__top < 0
    
    def size(self) -> int:
        return self.__top + 1
    
    def print(self) -> None:
        print(self.__arr)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.print()
    s.pop()
    s.pop()
    s.print()