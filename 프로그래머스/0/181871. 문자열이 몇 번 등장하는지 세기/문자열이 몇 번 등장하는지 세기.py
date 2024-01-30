def solution(myString, pat):
    count = 0
    start = 0

    while True:
        index = myString.find(pat, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break

    return count