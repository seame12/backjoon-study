def solution(my_string):
    answer = 0
    a=0
    for i in my_string:
        if i.isdigit():
            a=a*10+int(i)
        else:
            answer=answer+a
            a=0
    return answer+a