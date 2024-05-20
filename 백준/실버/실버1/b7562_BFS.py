# 나이트의 이동
# 백준/7562번

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2] # 이동 가능한 x 배열
    dy = [2, 2, 1, -1, -2, -2, -1, 1] # 이동 가능한 y 배열

    q = deque()
    q.append((now_X, now_Y)) # 첫 시작 지점 큐 삽입

    while q :
        # x, y를 popleft로 꺼내주기
        x, y = q.popleft() 

        # x와 y가 이동하려는 좌표인지 체크하기
        if x == dest_X and y == dest_Y : # 조건(이동하려는 칸과 일치)에 맞다면 
            return graph[x][y] - 1  # graph[x][y]에 저장된 값에서 -1을 출력해주기
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l : # 체스판을 벗어나지 않고
                if graph[nx][ny] == 0 : # 아직 방문하지 않았다면
                    graph[nx][ny] = graph[x][y] + 1 
                    q.append((nx, ny))


for _ in range(t):
    l = int(input())
    now_X, now_Y = map(int,input().split())
    dest_X, dest_Y = map(int,input().split())

    if now_X == dest_X and dest_X == dest_Y :
        print(0) 
        continue

    graph = [ [0] * l for _ in range(l)]
    graph[now_X][now_Y] = 1
    print(bfs())

