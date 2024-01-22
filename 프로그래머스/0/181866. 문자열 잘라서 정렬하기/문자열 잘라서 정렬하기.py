def solution(myString):
    answer = []
    answer=myString.split('x')
    answer=[v for v in answer if v]
    answer.sort()
    return answer