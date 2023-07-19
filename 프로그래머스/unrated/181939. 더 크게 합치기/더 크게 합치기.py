def solution(a, b):
    hap1=str(a)+str(b)
    hap2=str(b)+str(a)
    if int(hap1)>int(hap2):
        return int(hap1)
    return int(hap2)