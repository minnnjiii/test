# 백준/2178번
# 미로 탐색

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q =deque()
    q.append((x,y))

    while q : 
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 1 :
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                     
                    
    return graph[N-1][M-1]

N, M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)] 

print(bfs(0,0))