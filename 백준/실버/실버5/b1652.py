# 누울 자리를 찾아라 

# 영식이가 누울 수 있는 자리의 조건 
# 연속해서 2칸 이상의 빈칸이 존재하면 몸을 양 옆으로 쭉 뻗으며 누울 수 있음 
# 가로, 세로 둘 다 누울 수 있음 
# 중간에 어정쩡하게 눕는 경우가 없어 무조건 몸을 쭉 뻗어서 벽이나 짐에 닿게 됨 (즉 그 줄은 이제 못 누울 수 있는 경우 x)

N = int(input())

graph = [ '.'*N for _ in range(N)]


for i in range(N):
    for j in range(N):
        graph[i][j] = input().strip()

xCnt = 0
yCnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == '.' and j != N-1:
            if graph[i][j+1] == '.':
                xCnt += 1
                break 


for i in range(N):
    for j in range(N):
        if graph[j][i] == '.' and i != N-1:
            if graph[j][i+1] == '.':
                yCnt += 1
                break 

            
print(xCnt, yCnt)