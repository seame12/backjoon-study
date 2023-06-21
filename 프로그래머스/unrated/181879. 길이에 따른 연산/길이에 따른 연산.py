def solution(num_list):
    answer = 0
    result=1
    n=len(num_list)
    if n>=11:
        answer=sum(num_list)
    else:
        for i in num_list:
            result=result*i
        answer=result
    return answer