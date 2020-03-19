def no_teen_sum(a, b, c):
    return fix_teem(a) + fix_teem(b) + fix_teem(c)

def fix_teem(n):
    if n>=13 and n<=19:
        if n == 15 or n == 16:
            return n
        else:
            return 0
    else:
        return n
