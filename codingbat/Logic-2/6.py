def close_far(a, b, c):
    if abs(b-a) <= 1:
         close = b
    elif abs(c-a) <= 1: 
        close = c
    else:
        return False

    if (close == b) and (abs(c-a) >= 2) and (abs(c-b)>=2):
        return True
    elif (close == c) and (abs(b-a) >= 2) and (abs(b-c)>=2):
        return True
    else:
        return False
