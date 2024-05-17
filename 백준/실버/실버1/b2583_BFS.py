# 백준/2583번
# 영역 구하기
# 몇 개의 영역으로 분리되는지, 분리된 각 영역의 넓이가 얼마인지

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x,y))
    graph[x][y] = 1
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4) : 
            nx = dx[i] + x 
            ny = dy[i] + y

            if 0 <= nx < M and 0 <= ny < N :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    q.append((nx,ny))
                    size += 1
    result.append(size)


# M = 세로, N = 가로
M , N , K = map(int,input().split())
graph = [[0]*N for _ in range(M)] 

for _ in range(K) :
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(M-y1-1, M-y2-1, -1):
            graph[j][i] = 1


result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 :
            bfs(i,j)
result.sort()

print(len(result))
for i in result:
    print(i, end=' ')
        
        