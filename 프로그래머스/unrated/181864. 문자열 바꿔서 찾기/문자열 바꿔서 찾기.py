def solution(myString, pat):
    answer = 0
    b=[]
    a={"A":"B","B":"A"}
    for i in myString:
        b.append(a[i])
    c=''.join(b)
    if pat in c:
        return 1
    return 0