# DFS와 BFS
# 백준/1260번

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())

# N 정점의 개수
# M 간선의 개수
# V 탐색을 시작할 번호 

# 그래프 만들기
graph = [[] for _ in range(N + 1)]
# 그래프 채우기
for i in range(M):
    a, b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort() 

# DFS로 풀기
# DFS는 재귀로 구현합니다
visited_DFS = [0] * (N + 1) 
def dfs(N):
    visited_DFS[N] = 1 # 방문한거 흔적 남기기
    print(N, end=" ")
    for i in graph[N]:
        if not visited_DFS[i]: #방문하지 않은 곳이라면
            dfs(i) 


# BFS로 풀기
# BFS는 deque와 popleft로 구현합니다
visited_BFS = [0] * (N + 1)
def bfs():
    q = deque() # q에 덱 하나 만들어주기
    q.append(V) # 내가 출발할 위치인 V 넣기
    visited_BFS[V] = 1
    while q :
        node = q.popleft()
        print(node, end = " ")
        visited_BFS[node] = 1
        for i in graph[node]:
            if not visited_BFS[i] :
                q.append(i)
                visited_BFS[i] = 1

dfs(V)
print()
bfs()
