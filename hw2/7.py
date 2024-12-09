from stack import Stack

def find_bmm(first_num: int, second_num: int) -> int:
    if first_num < second_num:
        first_num, second_num = second_num, first_num
        # raise Exception("The First Number must be GREATER than the Second Number!")

    stack = Stack(2)

    while True:
        stack.push(second_num)
        stack.push(first_num)
        a = stack.pop()
        b = stack.pop()
        r = a % b
        if r == 0:
            return b
        first_num, second_num = second_num, r

print(find_bmm(12, 8))

# def recursive_bmm(first_num: int, second_num: int):
#     if first_num < second_num:
#         first_num, second_num = second_num, first_num
#
#     if first_num % second_num == 0:
#         return second_num
#
#     return recursive_bmm(second_num, first_num % second_num)

# print(recursive_bmm(26, 78))