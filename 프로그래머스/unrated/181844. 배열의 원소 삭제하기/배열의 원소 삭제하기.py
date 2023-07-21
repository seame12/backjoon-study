def solution(arr, delete_list):
    for i in delete_list:
        for j in arr:
            if j==i:
                arr.remove(i)
    return arr