# 백준/14940번
# 쉬운 최단거리

from collections import deque
import sys
input = sys.stdin.readline

# BFS 
def bfs(x,y):

    q = deque()
    q.append((x,y)) 

    visited[x][y] = 1 # 방문 처리해주기
    graph[x][y] = 0 

    while q :
        x, y  = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m : # 좌표를 벗어나지 않는다면
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    # 이동가능한 칸이고 방문한 칸이 아니라면
                    visited[nx][ny] = 1 # 우선 이제 방문했으니깐 방문처리
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                

n, m = map(int,input().split())
# n 세로 크기
# m 가로 크기

ans = []

# 그래프 만들기
graph = [list(map(int,input().split())) for _ in range(n)]

# 방문 여부 그래프 만들기
visited = [[0 for _ in range(m)] for _ in range(n)]


# 방향 탐색 범위 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기값 설정 
# 목적지 2부터 출발함 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: # 목적지라면
            x, y = i, j #x,y에 인덱스 저장하기

# 저장한 인덱스로 bfs 호출 
# 목적지 2부터 출발하는 것.
bfs(x, y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0 : # 갈 수 있는 곳이고 방문하지 않았다면
            graph[i][j] = -1

# 이제 끝 , 정답 출력해주기
for i in graph:
    for j in i :
        print(j, end = " ")
    print()