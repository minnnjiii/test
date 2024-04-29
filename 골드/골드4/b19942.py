# 다이어트
# 백준/19942번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999999)



N = int(input()) 
mp, mf, ms, mv = map(int,input().split())
nut = [list(map(int,input().split())) for _ in range(N)]

def recur(idx,a,b,c,d,price):
    global ans
    global res
    global cnt

    if idx == N:
        if a > mp and b > mf and c > ms and d > mv  : 
            ans = min(ans,price)
            res.append(price)
        return

    recur(idx+1,nut[idx][0]+a,nut[idx][1]+b,nut[idx][2]+c,nut[idx][3]+d,nut[idx][4]+price)
    recur(idx+1, nut[idx][0], nut[idx][1], nut[idx][2], nut[idx][3], nut[idx][4])


def _recur(_idx):

    if _idx == N:
        # 영양소 다 추가한조건 추가 
        print("success")
        return
    
    for i in range(N):
        return
   

res = []
ans = 1e9
cnt = 0

recur(0,0,0,0,0,0)
print(min(res))
print(ans)