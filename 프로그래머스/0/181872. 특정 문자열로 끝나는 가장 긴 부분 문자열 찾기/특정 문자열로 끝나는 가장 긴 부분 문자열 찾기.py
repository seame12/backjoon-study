def solution(myString, pat):
    a=myString.rindex(pat)+len(pat)
    return myString[:a]