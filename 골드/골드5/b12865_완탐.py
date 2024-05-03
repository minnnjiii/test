# 평범한 배낭
# 백준/12865번 

import sys
input = sys.stdin.readline

sys.setrecursionlimit(999999)
N, K = map(int,input().split())

bag = []
ans = 0

for _ in range(N):
    bag.append(list(map(int,input().split()))) 

def recur(idx, kilo, value ):
    global ans

    if kilo > K : return
    if idx == N : 
        ans = max(ans,value)
        return
    
    recur(idx+1,kilo+bag[idx][0],value+bag[idx][1])
    recur(idx+1,kilo, value)

recur(0,0,0)
print(ans)