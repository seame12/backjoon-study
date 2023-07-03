def solution(my_string, is_suffix):
    answer = 0
    answer_list = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in answer_list :
        answer=1
    return answer