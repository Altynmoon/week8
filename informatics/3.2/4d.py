n = int(input())

i = 0
power = 0
two = 1


while(two < n):
    while(i <= power):
        two *= 2
        i += 1
    power += 1


if(two == n):
    print("YES")
else:
    print("NO")