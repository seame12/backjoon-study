def solution(arr):
    answer = []
    n=len(arr)
    for i in range(n):
        if arr[i]==2:
            answer.append(i)
    if not answer:
        return [-1]
    else:
        return arr[answer[0]:answer[-1]+1]