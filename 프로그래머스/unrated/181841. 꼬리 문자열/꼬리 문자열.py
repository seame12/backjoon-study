def solution(str_list, ex):
    answer=[]
    for i in range(len(str_list)):
        if ex in str_list[i]:
            answer.append(str_list[i])
    for i in answer:
        str_list.remove(i)
    return ''.join(str_list)