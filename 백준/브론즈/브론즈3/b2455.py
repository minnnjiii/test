# 지능형 기차 

train = 0
ans = []
for i in range(4):
    minus, plus = map(int,input().split())
    train -= minus 
    train += plus 
    ans.append(train)

print(max(ans))