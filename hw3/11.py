from random import randint


def insertion_sort(arr): # O(n^2)
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

def merge_sort(arr): # O(nlogn)
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr): # worst case: O(n^2) , normal case: O(nlogn)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


list1 = [randint(0, 1_000_000) for _ in range(10000)]
list1[:len(list1)//2] = insertion_sort(list1[:len(list1)//2])
list1[len(list1)//2:] = quick_sort(list1[len(list1)//2:])
list1 = insertion_sort(list1)
print(list1)

list2 = [randint(0, 1_000_000) for _ in range(10000)]
list2 = insertion_sort(list2)
print(list2)

list3 = [randint(0, 1_000_000) for _ in range(10000)]
list3 = merge_sort(list3)
print(list3)

list4 = [randint(0, 1_000_000) for _ in range(10000)]
list4 = quick_sort(list4)
print(list4)