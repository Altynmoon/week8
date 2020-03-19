m = int(input())
n = input().split()
result = list(map(int, n))

counter = 0

for i, j in enumerate(result):
    if(i > 0 and result[i] > result[i - 1] and i < m):
        counter += 1

print(counter)