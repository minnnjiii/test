# 도영이가 만든 맛있는 음식
# 백준/2961번

# 곱 = 신맛 
# 합 = 쓴맛

import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999999)


N = int(input())

food = [ () for _ in range(N)]

for i in range(N):
    a,b = map(int,input().split())
    food[i] += (a,b)

def recur(idx,sin,son,use):
    global ans

    if idx == N : 
        if use > 0:
            ans = min(ans,abs(sin - son))
        return
    
    recur(idx+1, sin * (food[idx][0]), son + (food[idx][1]), use+1)
    recur(idx+1,sin,son,use)

ans = 1e9
recur(0,1,0,0)

print(ans)


