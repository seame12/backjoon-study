import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))

answer = []
for i in a:
    if i < m:
        answer.append(str(i))
print(' '.join(answer))