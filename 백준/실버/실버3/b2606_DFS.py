# 백준/2606번
# 바이러스

# DFS 풀이
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수
M = int(input()) # 서로 연결되어 있는 컴퓨터 쌍의 수 

graph = [[] for _ in range(N+1)] # 그래프 만들기 


# 이미 방문했던 node를 다시 방문하는 것을 막기 위해
# visited 함수 만들기
visited = [0 for _ in range(N+1)] 
# visited[1] = 0
# visited[1] = 1


# 그래프 채우기
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# graph[1] = [2,5]
# graph[2] = [1,3,5]
# graph[3] = [2]
# graph[4] = [7]
# graph[5] = [6]
# graph[6] = [1,2,6]
# graph[7] = [4]


# 재귀 함수 만들기
def recur(node):

    # 방문한 거 흔적 남기기 
    visited[node] = 1

    # 연결된 node들 차례대로 불러오기
    for next in graph[node]:


        # 만약 방문했다면
        if visited[next] == 1 : 
            # 넘어가!!!
            continue

        # 재귀함수 부르기
        recur(next)

# 1번 컴퓨터가 웜 바이러스에 걸린거니까 시작은 1
recur(1)

print(sum(visited)-1)
