def solution(myString, pat):
    longest_suffix = ""
    current_suffix = ""

    for char in myString:
        current_suffix += char
        if current_suffix.endswith(pat):
            longest_suffix = current_suffix

    return longest_suffix