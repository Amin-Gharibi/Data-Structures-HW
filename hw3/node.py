class DoublyNode:
    def __init__(self, data: any) -> None:
        self.data = data
        self.prev = None
        self.next = None

class SingleNode:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None