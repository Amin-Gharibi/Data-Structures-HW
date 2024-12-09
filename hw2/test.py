def func(arr, value):
    if len(arr) == 1:
        return arr[0] == value

    if value < arr[len(arr)//2]:
        return func(arr[:len(arr)//2], value)
    else:
        return func(arr[len(arr)//2+1:], value)

print(func([1,2,3,8], 4))
