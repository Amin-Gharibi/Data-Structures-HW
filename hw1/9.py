arr = [1, 3, 2]

def func1(arr: list, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left == right:
        return arr[left]
    
    max_left = func1(arr, left, (left+right)//2)
    max_right = func1(arr, (left+right)//2 + 1, right)

    return max(max_left, max_right)


print(func1(arr))

"""
    COMPLEXITY:

    T(n) = aT(n/b) + f(n)
    a: 2 because it calls itself twice in each round of running
    b: 2 because the whole problem gets half in each round of running
    f(n): 3, one for max_left, one for max_right and the last one for max(max_left, max_right) so it's O(1)

    log a_b => log 2_2: 1
    n^(log a_b) => n^1
    f(n) <= n or f(n) = O(n) so the answer would be T(n) = Θ(n)
"""

def func2(arr: list, index=1, biggest=None):
    if biggest is None:
        biggest = arr[0]

    if index == len(arr):
        return biggest

    biggest = max(biggest, arr[index])
    return func2(arr, index+1, biggest)

"""
    COMPLEXITY:

    T(n) = aT(n/b) + f(n)
    a: 1 because it calls itself once in each round of running
    b: 1 because the whole problem gets smaller by one element in each round of running
    f(n): 2, one for defining biggest var and another one for max(biggest, arr[index]) so it's O(1)

    so it would be: T(n) = T(n-1) + O(1)

    log a_b => log 1_1: 1
    n^(log a_b) => n^1
    f(n) <= n or f(n) = O(n) so the answer would be T(n) = Θ(n)
"""