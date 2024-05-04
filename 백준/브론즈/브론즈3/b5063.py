# TGN
# 5063번

n = int(input()) 

# r은 광고를 하지 않았을 때 수익
# e는 광고를 했을 때의 수익
# c는 광고 비용

for i in range(n) : 
    r,e,c = map(int,input().split()) 
    if (e-c) > r : 
        print("advertise")
    elif (e-c) == r :
        print("does not matter")
    else:
        print("do not advertise")