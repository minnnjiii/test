# 백준/2589번
# 보물섬

# BFS
import sys
sys.setrecursionlimit(999999999)
from collections import deque
import sys
input = sys.stdin.readline

Y, X = map(int,input().split()) 
graph = [list(map(str,input().strip())) for _ in range(Y)]


maxi = 0

for y in range(Y) :
    for x in range(X) :
        if graph[y][x] == 'L' :
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]

            #BFS
            q = deque()
            q.append([y,x]) # 시작점
            visited[y][x] = 1
            while q:
                ey, ex = q.popleft()

                # 4방향 탐색! 2차원 DP
                for dy, dx in [[0,1],[1,0],[-1,0],[0,-1]] :
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < Y and 0 <= nx < X :
                        if graph[ny][nx] == 'L' :
                            if visited[ny][nx] == 0 : # 방문한적이 없다면
                                visited[ny][nx] = 1 
                                dist[ny][nx] = max(dist[ey][ex] + 1, dist[ny][nx])
                         
                                
                                if maxi < dist[ny][nx] :
                                    maxi = dist[ny][nx]
                                
                                q.append((ny,nx))
            if maxi == X + Y - 2 :
                            break

print(maxi)