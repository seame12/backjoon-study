import sys
n,m=map(int,input().split())
num_list=[0]*n
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        num_list[j-1]=c
print(' '.join(map(str, num_list)))