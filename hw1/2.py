arr = [1, 2, 3, 4, 5]
# inner loop which adds up list items and returns the new arr
def add_list_numbers(arr: list, new_arr=None, index=None):
    if new_arr is None:
        new_arr = []
    if index is None:
        index = 0

    if index == len(arr) - 1:
        return new_arr
    
    new_arr.append(arr[index] + arr[index + 1])
    return add_list_numbers(arr, new_arr, index+1)

# the main recursive func
def recursive_func(arr: list):
    print(arr)
    if len(arr) == 1:
        return arr
    
    new_arr = add_list_numbers(arr)
    return recursive_func(new_arr)


recursive_func(arr)
# func(arr)