# 주사위 게임 
# 10103번 


c = s = 100 # c 창영 s 상덕 초기 점수

n = int(input()) # 라운드 수 
for i in range(n) : 
    cscore, sScore = map(int,input().split()) 
    if cscore == sScore : 
        pass
    elif cscore > sScore : 
        s -= cscore
    else : 
        c -= sScore

print(c)
print(s)