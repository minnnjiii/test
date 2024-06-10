# 최단경로
# 백준/1753번

from collections import deque
import sys
input = sys.stdin.readline

# 정점의 개수 V, 간선의 개수 E
V, E = map(int,input().split()) 

# 시작 정점의 번호 K
K = int(input())

# graph 만들기 
links = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)] # BFS를 하려면 visit 처리를 해줘야함!

# 각 간선을 나타내는 세 개의 정수 u, v, w 입력 받기
# u에서 v로 가는 가중치 w인 간선
for _ in range(E):
    u,v,w = map(int,input().split())
    links[u].append([v,w])

# BFS
q = deque()
q.append(K) 
visited

dijkstra = [0 * (V)]

for i in range(E) : 
    dijkstra[i] = K 


# for i in range(E):
#     if graph[i][0] == K :
#         for j in range(E):
#             if graph[i][1] == K + j + 1 :
#                 print(graph[i][2])
#             else: 

