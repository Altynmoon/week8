def lone_sum(a, b, c):
    if a == b == c:
        return 0 
    elif a == b: 
        return c 
    if a == c: 
        return b 
    elif b == c: 
        return a
    else:
        return a + b + c
print(lone_sum(3,4,4))