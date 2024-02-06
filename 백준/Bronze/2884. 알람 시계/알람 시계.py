n, m = map(int, input().split())  
if n == 0:
    if m >= 45:
        m -= 45
    else:
        m += 15
        n = 23
else:
    if m >= 45:
        m -= 45
    else:
        m += 15
        n -= 1
print(n, m)