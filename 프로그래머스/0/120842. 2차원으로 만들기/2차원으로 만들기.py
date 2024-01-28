def solution(num_list, n):
    a = len(num_list)
    b = a // n
    answer = [[0] * n for _ in range(b)]

    for i in range(a):
        row = i // n
        col = i % n
        answer[row][col] = num_list[i]

    return answer