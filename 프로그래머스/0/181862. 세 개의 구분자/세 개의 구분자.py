def solution(myStr):
    space={"a":" ","b":" ","c":" "}
    myStr2 = ''.join(space.get(char, char) for char in myStr)
    a=myStr2.split(' ')
    b = [i for i in a if i != ""]
    if b:
        return b
    else:
        return ["EMPTY"]