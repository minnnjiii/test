# 단지번호붙이기
# 백준/2667번

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0 , 0]
dy = [ 0, 0, -1, 1]


def bfs(graph, a,b):


    q = deque()
    q.append([a,b])
    graph[a][b] = 0
    size = 1
    while q : 
        x,y = q.popleft()
        graph[x][y] = 0 
        for i in range(4) : 
            
            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < N and 0 <= ny < N :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0 
                    q.append([nx,ny])
                    size += 1
    return size


N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)] 
result = [] 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 :
            size = bfs(graph,i,j)
            result.append(size)
result.sort()  # 오름차순으로 정렬

print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)