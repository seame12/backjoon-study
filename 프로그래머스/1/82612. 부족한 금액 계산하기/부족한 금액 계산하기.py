def solution(price, money, count):
    answer = 0
    a=0
    for i in range(1,count+1):
        a=a+i
    price=price*a
    if price-money>0:
        return abs(money-price)
    else:
        return 0