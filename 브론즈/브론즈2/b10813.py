# 공 바꾸기_10813번

N, M = map(int,input().split())

b = [i for i in range(1,N+1)]

for i in range(M):
    i, j = map(int,input().split())
    b[i-1],b[j-1] = b[j-1],b[i-1]
    
for i in range(N):
    print(b[i], end=' ')