n = int(input())

power = 0
i = 0
two = 1

while(two < n):
    while(i <= power):
        two *= 2
        i += 1
    power +=1

print(power)