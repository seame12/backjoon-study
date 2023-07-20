def solution(my_string):
    answer=''
    for i in my_string:
        if ord(i)>96:
            answer=answer+i.upper()
        else:
            answer=answer+i.lower()
    return answer