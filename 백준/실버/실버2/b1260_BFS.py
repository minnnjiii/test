# DFS와 BFS
# 백준/1260번

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())

# N 정점의 개수
# M 간선의 개수
# V 탐색을 시작할 번호 

graph = [[] for _ in range(N + 1)]
visited_DFS = [0] * (N + 1) 

for i in range(M):
    a, b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort() 

def dfs(N):
    visited_DFS[N] = 1
    print(N, end=" ")
    for i in graph[N]:
        if not visited_DFS[i]:
            dfs(i)

dfs(V)
print()

visited_BFS = [0] * (N + 1)


def bfs():
    q = deque()
    q.append(V)
    visited_BFS[V] = 1
    while q :
        node = q.popleft()
        print(node, end = " ")
        visited_BFS[node] = 1
        for i in graph[node]:
            if not visited_BFS[i] :
                q.append(i)
                visited_BFS[i] = 1

bfs()
