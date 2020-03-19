m = int(input())
n = input().split()
result = list(map(int, n))

for i, j in enumerate(result):
    if(i >= m):
        break
    if(j % 2 == 0):
        print(j, end = " ")