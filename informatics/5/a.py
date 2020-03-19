n = input().split()
array = list(map(int, n))

def findMin(a, b, c, d):
    return min(a, b, c, d)

answer = findMin(array[0], array[1], array[2], array[3])
print(answer)
    