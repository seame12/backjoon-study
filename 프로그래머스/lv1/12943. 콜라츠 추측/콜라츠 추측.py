def solution(num):
    i=0
    while num!=1 :
        if num%2==0:
            num=num/2
        else :
            num=num*3+1
        i=i+1
    if i>=500:
        return -1
    return i