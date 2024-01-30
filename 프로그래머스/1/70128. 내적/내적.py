def solution(a, b):
    answer = 0
    c=len(a)
    for i in range(c):
        answer=answer+a[i]*b[i]
    return answer