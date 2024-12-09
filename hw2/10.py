from queue_structure import Queue

class StackUsingQueue:
    def __init__(self, max_size: int) -> None:
        self.__max_size = max_size
        self.__first_queue = Queue(self.__max_size)
        self.__second_queue = Queue(self.__max_size)
    
    def isFull(self) -> bool:
        return self.__first_queue.isFull()
    
    def isEmpty(self) -> bool:
        return self.__first_queue.isEmpty()
    
    def size(self) -> int:
        return self.__first_queue.size()
    
    def push(self, value: any) -> None: # O(n)
        if self.isFull():
            raise Exception("StackUsingQueue is Full, you can't push!")
        
        self.__second_queue.enqueue(value)
        while not self.__first_queue.isEmpty():
            self.__second_queue.enqueue(self.__first_queue.dequeue())
        
        self.__first_queue, self.__second_queue = self.__second_queue, self.__first_queue
    
    def pop(self) -> any: # O(1)
        if self.__first_queue.isEmpty():
            raise Exception("StackUsingQueue is Empty, you can't pop!")
        
        return self.__first_queue.dequeue()
    
    def peek(self) -> any: # O(1)
        if self.__first_queue.isEmpty():
            raise Exception("StackUsingQueue is Empty, you can't peek!")

        return self.__first_queue.peek()
    
    def print(self) -> None: # O(1)
        if self.isEmpty():
            print("StackUsing Queue is empty")
            return

        self.__first_queue.print()


stack = StackUsingQueue(3)
stack.push(1)
stack.push(2)
stack.push(3)
# stack.pop()
stack.print()