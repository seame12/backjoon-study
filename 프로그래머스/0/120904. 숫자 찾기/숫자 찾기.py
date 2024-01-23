def solution(num, k):
    answer = 0
    a=str(num)
    b=str(k)
    if b in a:
        return int(a.index(b))+1
    else :
        return -1