def solution(order):
    a=str(order)
    b=0
    for i in a:
        if i!='0' and int(i)%3==0:
            b=b+1
    return b