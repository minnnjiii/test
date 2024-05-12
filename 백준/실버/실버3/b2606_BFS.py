# 백준/2606번
# 바이러스

# BFS 풀이
from collections import deque

import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수
M = int(input())  # 서로 연결되어 있는 컴퓨터 쌍의 수 

graph = [[] for _ in range(N+1)] 

visited = [0 for _ in range(N+1)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# q에 덱을 하나 만들어주기
q = deque()

# q에 내가 출발할 위치인 1을 넣어줍니다 
q.append(1)

# popleft를 쓰는 이유는 인접한 애들부터 접근하니까
while len(q) > 0 : 
    node = q.popleft() # 처음엔 1
    visited[node] = 1 
    
    for next in graph[node] : 
        if visited[next] == 1:
            continue
        q.append(next) 

print(sum(visited) -1)

