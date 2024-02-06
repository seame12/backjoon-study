n, m = map(int, input().split())
t=int(input())
m += t
n += m // 60
m %= 60
n %= 24

print(n, m)