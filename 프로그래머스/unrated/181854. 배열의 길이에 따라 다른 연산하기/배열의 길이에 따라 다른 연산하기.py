def solution(arr, n):
    a=len(arr)
    if a%2==1:
        for i in range(a):
            if i%2==0:
                arr[i]+=n
    else:
        for i in range(a):
            if i%2==1:
                arr[i]+=n       
            
    return arr