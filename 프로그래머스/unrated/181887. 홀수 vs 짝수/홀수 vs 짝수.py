def solution(num_list):
    a=0
    b=0
    for i in range(len(num_list)):
        if (i+1)%2==0:
            a=a+num_list[i]
        else :
            b=b+num_list[i]
    if a-b>0:
        return a
    else :
        return b