m = int(input())
n = input().split()

array = list(map(int, n))

newArr = []

for i, j in enumerate(array):
    if(i < m):
        newArr.append(j)

for i in reversed(newArr):
    print(i, end = " ")