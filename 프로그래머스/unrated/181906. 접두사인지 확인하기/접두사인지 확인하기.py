def solution(my_string, is_prefix):
    if is_prefix in my_string:
        if my_string[1]==is_prefix[1] and my_string[0]==is_prefix[0]:
            return 1
    return 0