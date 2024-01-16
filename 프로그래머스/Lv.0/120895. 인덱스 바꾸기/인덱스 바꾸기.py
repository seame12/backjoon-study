def solution(my_string, num1, num2):
    answer = ''
    a=list(my_string)
    b=a[num1]
    c=a[num2]
    a[num1]=c
    a[num2]=b
    return "".join(a)