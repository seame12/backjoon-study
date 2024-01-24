def solution(a, d, included):
    answer=0
    n=len(included)
    num = [a + i * d for i in range(n)]
    for j in range(n):
        answer=answer+num[j]*included[j]
    return answer