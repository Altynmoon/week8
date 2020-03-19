n = input().split()
array = list(map(float, n))

def power(a, n):
    return a ** n


print(power(array[0], array[1]))