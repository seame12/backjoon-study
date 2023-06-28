def solution(myString):
    answer=''
    z=myString.lower()
    for i in z:
        if i=='a':
            answer=answer+'A'
        else:
            answer=answer+i
    return answer