# 누울 자리를 찾아라 

# 영식이가 누울 수 있는 자리의 조건 
# 연속해서 2칸 이상의 빈칸이 존재하면 몸을 양 옆으로 쭉 뻗으며 누울 수 있음 
# 가로, 세로 둘 다 누울 수 있음 
# 중간에 어정쩡하게 눕는 경우가 없어 무조건 몸을 쭉 뻗어서 벽이나 짐에 닿게 됨 (즉 그 줄은 이제 못 누울 수 있는 경우 x)

N = int(input())

graph = [] 

for _ in range(N):
    graph.append(list(input().strip()))  # 한 줄씩 입력받기


xCnt = 0 # 가로로 누울 수 있는 자리의 수
yCnt = 0 # 세로로 누울 수 있는 자리의 수 

# 가로 탐색
for i in range(N): 
    x = 0 # 한 줄에 X가로 가로막혀 있다면 다시 누울 수 있으므로 그걸 활용해 .을 세어줄 변수 
    for j in range(N): 
        if graph[i][j] == '.': # 누울 수 공간이라면
            x += 1 # 하나 추가! 
            if x == 2 : # 만약 .이 2개로 누울 수 있는 공간이 충족됐다면
                xCnt += 1 # 가로로 누울 수 있는 자리의 수 추가! 
        else : 
            x = 0

# 세로 탐색
for i in range(N):
    y = 0
    for j in range(N):
        if graph[j][i] == '.':
            y += 1
            if y == 2 : 
                yCnt += 1
        else : 
            y = 0

            
print(xCnt, yCnt)