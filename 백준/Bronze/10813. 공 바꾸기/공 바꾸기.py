import sys
n, m = map(int, sys.stdin.readline().split())
num_list=[i for i in range(1, n+1)]
for j in range(m):
    a, b = map(int, sys.stdin.readline().split())
    num_list[a-1], num_list[b-1] = num_list[b-1], num_list[a-1]
print(*num_list)