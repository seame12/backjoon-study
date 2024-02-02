def solution(s):
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    once = [j for j, l in count.items() if l == 1]

    return ''.join(sorted(once))