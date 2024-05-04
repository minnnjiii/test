# 주사위 게임
#2476

money = []
n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if a == b == c :
        money.append( (10000 + (a * 1000)))
    elif a == b  :
        money.append((1000 + (a * 100)))
    elif a == c  :
        money.append((1000 + (a * 100)))
    elif c == b  :
        money.append((1000 + (b * 100)))
            
    elif a != b and b!= c and c!= a : 
        money.append( ( max(a,b,c) * 100 ))

print(max(money))