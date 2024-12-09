from random import randint
from max_heap import MaxHeap

max_heap = MaxHeap()
arr = [randint(1, 100) for _ in range(100)]
max_heap.heapify(arr)
max_heap.insert(4)
max_heap.insert(18)
max_heap.insert(11)
max_heap.insert(2)
max_heap.extract_max()
max_heap.extract_max()
max_heap.insert(13)
max_heap.insert(5)
max_heap.insert(1)
max_heap.extract_max()

print(max_heap.heap)