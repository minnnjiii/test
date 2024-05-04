# 욕심쟁이 판다
# 백준/1937번

# 2차원 DP
# 2차원 그래프에서 DP를 해보자!
# 경우의 수(재귀) -> DP에 저장하고 -> 점화식! 

# 알고리즘 분류 
# - 다이나믹 프로그래밍
# - 그래프 이론
# - 그래프 탐색
# - 깊이 우선 탐색

import sys
input = sys.stdin.readline

sys.setrecursionlimit(99999999)
def recur(y,x):

    if dp[y][x] != 0 :
        return dp[y][x]
    
    for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
        ey = y + dy
        ex = x + dx

        # 그래프를 벗어나지 않고 그 안에서만 이동함
        if 0 <= ey < n and 0 <= ex < n : 
            # 내 위치보다 이동할 위치가 더 큰 경우에만 이동함
            if graph[y][x] < graph[ey][ex] : 
                dp[y][x] = max(dp[y][x], recur(ey,ex) + 1)
    
    return dp[y][x]
    
n = int(input()) 

graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur(y,x)
   

print(max(map(max,dp)) +1)