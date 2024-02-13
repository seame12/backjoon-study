def solution(emergency):
    answer = []
    sunseo=sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(sunseo.index(i)+1)
    return answer