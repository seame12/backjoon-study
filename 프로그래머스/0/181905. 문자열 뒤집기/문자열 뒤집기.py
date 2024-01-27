def solution(my_string, s, e):
    a = my_string[s:e+1]
    b = a[::-1]
    
    result = my_string[:s] + b + my_string[e+1:]
    return result