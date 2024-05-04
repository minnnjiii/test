# 가희와 방어율 무시
# 25238번

a, b = map(int,input().split())

defense = a * ( b/100)


if a - defense >= 100: 
    print(0)
else:
    print(1)