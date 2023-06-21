def solution(sides):
    answer = 0
    sides.sort()
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if c<a+b:
        answer=1
    else:
        answer=2
    return answer