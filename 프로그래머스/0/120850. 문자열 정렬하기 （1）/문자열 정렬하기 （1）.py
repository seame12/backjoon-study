def solution(my_string):
    numbers = [int(ch) for ch in my_string if ch.isdigit()]
    answer = sorted(numbers)
    return answer