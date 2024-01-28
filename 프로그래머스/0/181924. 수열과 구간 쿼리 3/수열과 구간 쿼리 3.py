def solution(arr, queries):
    for i in queries:
        c=0
        c=arr[i[0]]
        arr[i[0]]=arr[i[1]]
        arr[i[1]]=c
    return arr