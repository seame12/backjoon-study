def solution(num_list):
    num_list.sort()
    del num_list[:5]
    return num_list