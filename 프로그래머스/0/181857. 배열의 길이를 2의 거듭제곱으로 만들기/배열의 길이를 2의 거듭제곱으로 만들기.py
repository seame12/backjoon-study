def solution(arr):
    n=len(arr)
    while n & (n-1):
        arr.append(0)
        n=len(arr)
    return arr