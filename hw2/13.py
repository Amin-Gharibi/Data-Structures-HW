from stack import Stack

def find_longest_descending_sublist(target_arr):
    helper_stack = Stack()
    max_len, current_start, max_start, max_end = 0, 0, 0, 0

    for i in range(len(target_arr)):
        if helper_stack.isEmpty() or target_arr[i] <= helper_stack.peek():
            helper_stack.push(target_arr[i])
        else:
            if helper_stack.size() > max_len:
                max_len = helper_stack.size()
                max_start = current_start
                max_end = i # it must be i - 1 but because at the end we print i+1 we cancel-out 1's
            while not helper_stack.isEmpty():
                helper_stack.pop()
            helper_stack.push(target_arr[i])
            current_start = i

    if helper_stack.size() > max_len:
        max_len = helper_stack.size()
        max_start = current_start
        max_end = len(target_arr)

    return max_len, target_arr[max_start:max_end]

print(find_longest_descending_sublist([8,6,5,2,1,10,12,2]))