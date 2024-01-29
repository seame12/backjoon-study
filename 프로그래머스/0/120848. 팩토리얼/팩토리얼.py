def solution(n):
    if n == 0:
        return 1
    answer = 1
    a = 1

    while answer <= n:
        a += 1
        answer *= a

    return a - 1