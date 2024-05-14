# 백준/1926번
# 그림

from collections import deque
import sys
input = sys.stdin.readline

Y, X = map(int,input().split()) 
graph = [list(map(int,input().split())) for _ in range(Y)]

maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 1 : 
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]

            # BFS
            q = deque()
            q.append([y,x])
            visited[y][x] = 0 
            while q :
                ey, ex = q.popleft()

                for dy,dx in [[0,1],[1,0],[-1,0],[0,-1]] :
                    ny, nx = ey + dy, ex + dx 
                    if 0 <= ny < Y and 0 <= nx < X :
                        if graph[ny][nx] == 1 :
                            if visited[ny][nx] == 1 :
                                visited[ny][nx] = 0
                                dist[ny][nx] = max(dist[ey][ex] + 1, dist[ny][nx])
                                if maxi < dist[ny][nx] :
                                    maxi = dist[ny][nx]

                                q.append((ny,nx))

print(maxi)