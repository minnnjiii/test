# 내리막 길
# 백준/1520번
  

import sys
input = sys.stdin.readline

sys.setrecursionlimit(99999)

def recur(y,x):

    # 오른쪽 아래 지점까지 경로에 도달했다면 
    if y == Y-1 and x == X-1 : 
        return 1 
    
    # 이미 계산이 된거라면
    if dp[y][x] != -1 : 
        return dp[y][x]
    
    route = 0

    # 상하좌우로 움직이는 모든 경우의 수를 for문으로 계산
    for dy,dx in [[0,1],[0,-1],[-1,0],[1,0]]: 
        # ey는 현재 y위치에서 dy를 더한 값
        ey = y + dy
        # ex는 현재 x위치에서 dx를 더한 값
        ex = x + dx 

        # 좌표를 벗어나지 않았다면
        if 0 <= ey < Y and 0 <= ex < X : 
            # 현재 위치보다 이동하려는 위치의 값이 더 작다면
            if graph[y][x] > graph[ey][ex]:
                # route 값에 다시 이동하려는 위치를 재귀함수로 구함 
                route += recur(ey,ex)

    # dp값 저장
    dp[y][x] = route

    return dp[y][x]

Y, X = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(Y)] 

dp = [[-1 for _ in range(X)] for _ in range(Y)] 
answer = recur(0,0)
print(answer)