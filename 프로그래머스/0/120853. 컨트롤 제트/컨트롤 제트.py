def solution(s):
    answer = 0
    a=s.split(' ')
    for i in range(len(a)):
        if a[i]!='Z':
            answer+=int(a[i])
        else:
            answer-=int(a[i-1])
    return answer