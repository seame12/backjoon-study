def solution(numLog):
    answer = ''
    a=len(numLog)
    for i in range(1,a):
        b=numLog[i]-numLog[i-1]
        if b==1:
            answer=answer+'w'
        elif b==10:
            answer=answer+'d'
        elif b==-1:
            answer=answer+'s'
        else :
            answer=answer+'a'
    return answer