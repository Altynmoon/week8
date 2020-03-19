n = input().split()
arr = list(map(int, n))

def xor(a, b):
    if(a == b):
        return 0
    if(a or b):
        return 1

print(xor(arr[0], arr[1]))