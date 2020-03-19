m = int(input())
n = input().split()
result = list(map(int, n))

counter = 0

for i, j in enumerate(result):
    if(i >= m):
        break
    if(j > 0):
        counter += 1

print(counter)