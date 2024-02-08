import sys
n = int(input())
a = list(map(int, input().split()))
a_max=max(a)
a_min=min(a)
print(f"{a_min} {a_max}")