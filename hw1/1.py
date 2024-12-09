def ackermann(m: int, n: int):
    if m == 0 and n >= 0:
        return n+1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print(ackermann(7,7))