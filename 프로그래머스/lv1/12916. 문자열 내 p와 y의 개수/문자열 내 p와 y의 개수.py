def solution(s):
    answer = True
    pp=0
    yy=0
    
    for i in s.lower():
        if i=='p':
            pp=pp+1
        elif i=='y':
            yy=yy+1
    if pp!=yy:
        answer=False
    return answer