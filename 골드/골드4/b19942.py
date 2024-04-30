# 다이어트
# 백준/19942번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999999)

def recur(idx,protein,b,c,d,price):
    global ans
    global used
    global ans_used

    if protein >= mp and b >= mf and c >= ms and d >= mv  : 
        if ans > price:
            ans = min(ans,price)
            ans_used = []
            for i in used:
                ans_used.append(i)


    if idx == N:
        return
    
    used.append(idx+1)
    recur(idx+1,nut[idx][0]+protein,nut[idx][1]+b,nut[idx][2]+c,nut[idx][3]+d,nut[idx][4]+price)
 
    used.pop()
    recur(idx+1, protein, b, c, d, price)




N = int(input()) 
mp, mf, ms, mv = map(int,input().split())
nut = [list(map(int,input().split())) for _ in range(N)]

ans = 1e9
ans_used = []
used = []

recur(0,0,0,0,0,0)

ans_used.sort()
if ans:
    print(ans)
    print(*ans_used)

else:
    print(-1)