# 공 넣기

N, M = map(int,input().split())
list = [0] * N


for _ in range(M):
    i, j , k = map(int,input().split())
    for ball in range(i, j+1):
        list[ball-1] = k 
for i in range(N):
    print(list[i], end = ' ')
    