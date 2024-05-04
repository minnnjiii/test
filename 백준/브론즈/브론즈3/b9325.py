# 얼마?
# 9325

t = int(input()) 

for i in range(t):
    price = 0 
    s = int(input()) # 자동차의 가격
    price += s
    n = int(input()) # 해빈이가 구매하려고 하는 서로 다른 옵션의 개수
    for i in range(n) : 
        q,p = map(int,input().split()) 
        # q는 해빈이가 사려고 하는 특정 옵션의 개수이고 p는 해당 옵션의 가격
        price += q*p 

    print(price)