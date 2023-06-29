def solution(num_list):
    hap=0
    gop=1
    for i in num_list:
        hap=hap+i
        gop=gop*i
    if hap**2>gop:
        answer=1
    else:
        answer=0
    return answer