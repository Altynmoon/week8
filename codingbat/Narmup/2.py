def front_times(str,n):
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    result = ''
    for i in range(n):
        result += front
    return result 
print(front_times('Altynai', 3))