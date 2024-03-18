# 상금 헌터
# 15953


t = int(input()) 

for i in range(t) : 
    # 1회 a등, 2회 b등
    a,b = map(int,input().split()) 
    money = 0 
    if a == 0 : 
        pass
    elif a == 1 : 
        money += 5000000 
    elif a < 4 : 
        money += 3000000
    elif a < 7 : 
        money += 2000000 
    elif a < 11 : 
        money += 500000 
    elif a < 16 : 
        money += 300000 
    elif a < 22 : 
        money += 100000 
    
    if b == 0 :
        pass
    elif b == 1 : 
        money += 5120000
    elif b < 4 : 
        money += 2560000 
    elif b < 8 : 
        money += 1280000
    elif b < 16 : 
        money += 640000
    elif b < 32 : 
        money += 320000

    print(money)