class Queue:
    def __init__(self, size: int = float('inf')) -> None:
        self.__queue = []
        self.__max_size = size

    def isEmpty(self) -> bool:
        return len(self.__queue) == 0

    def isFull(self) -> bool:
        return len(self.__queue) == self.__max_size

    def enqueue(self, item: any) -> None:
        if self.size() > self.__max_size:
            raise Exception("Queue is full, you can not enqueue!")
        self.__queue.insert(0, item)

    def dequeue(self) -> any:
        if self.isEmpty():
            raise Exception("Queue is empty, you can not dequeue!")
        return self.__queue.pop()

    def size(self) -> int:
        return len(self.__queue)

    def peek(self) -> any:
        if self.isEmpty():
            raise Exception("Queue is empty, you can not get the peek!")
        return self.__queue[-1]

    def print(self) -> None:
        print(self.__queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print()
    
    print("Dequeued:", queue.dequeue())
    queue.print()
