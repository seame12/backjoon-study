def solution(num_list, n):
    answer = []
    if len(num_list)%n==0:
        for i in range(len(num_list)//n):
            answer.append(num_list[n*i])
    else:
        for i in range(len(num_list)//n+1):
            answer.append(num_list[n*i])
    
    return answer