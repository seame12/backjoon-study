def solution(x):
    a=str(x)
    ha=0
    for i in a:
        ha=ha+int(i)
    if x%ha==0:
        return True
    else :
        return False