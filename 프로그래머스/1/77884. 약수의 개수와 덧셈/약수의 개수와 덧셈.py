def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        r = int(i**0.5)
        if r * r == i:
            answer=answer-i
        else:
            answer=answer+i
    return answer