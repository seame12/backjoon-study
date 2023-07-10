def solution(absolutes, signs):
    a=[]
    for i in range(len(absolutes)):
        if signs[i]:
            a.append(absolutes[i])
        else:
            a.append(-1*absolutes[i])
    return sum(a)
        