def solution(board, k):
    answer = 0
    row_len = len(board)
    col_len = len(board[0])

    for i in range(row_len):
        for j in range(col_len):
            if i + j <= k :
                answer += board[i][j]

    return answer