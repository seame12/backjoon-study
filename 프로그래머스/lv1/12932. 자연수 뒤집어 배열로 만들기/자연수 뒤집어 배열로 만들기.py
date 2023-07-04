def solution(n):
    a=str(n)
    answer=[]
    for i in range(1,len(a)+1):
        b=int(a[-i])
        answer.append(b)
        
    return answer