def solution(i, j, k):
    answer = 0
    a=""
    for l in range(i,j+1):
        a=a+str(l)
    for m in a:
        if m==str(k):
            answer=answer+1
    return answer