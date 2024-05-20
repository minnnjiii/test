# 백준/1697번
# 숨바꼭질
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k :
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx] :
                dist[nx] = dist[x] + 1
                q.append(nx) 

MAX = 10 ** 5
dist = [0] * (MAX + 1) 
n, k = map(int, input().split()) # 수빈이가 있는 위치 n, 동생이 있는 위치 k

bfs()