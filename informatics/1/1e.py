s = 109
v = int(input())
t = int(input())

if(v < 0):
    kilometersBehind = 109+(v*t)
else:    
    kilometersBehind = v*t

print(kilometersBehind % s)