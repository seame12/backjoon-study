def solution(arr):
    n=len(arr)
    c=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==arr[j][i]:
                c=c+1
    if c==n*n:
        return 1
    else:
        return 0