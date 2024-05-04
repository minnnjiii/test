# 삼각 김밥
# 백준/2783번

sevenX, sevenY = map(int,input().split())

gimbap = []
for _ in range(int(input())):
    x, y = map(int,input().split())
    price = (x/y) * 1000
    gimbap.append(price) 


seven = (sevenX / sevenY ) * 1000
gimbap.append(seven)

print("{:.2f}".format(round(min(gimbap),2)))