# 구간 합 구하기 5
# 백준/11660번 

import sys
input = sys.stdin.readline

N , M = map(int,input().split())

graph = [list(map(int,input().split() ))for _ in range(N)]

# for문을 한 번 더 반복하면서 2차원 누적합을 만들어줌
prefix = [[ 0 for _ in range(N+1)] for _ in range(N+1)] 


    
# 누적합 표 만들기
for y in range(N):
    for x in range(N): 
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]
   
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split()) 

    # 누적합표에 따른 계산
    answer = prefix[x2][y2] - (prefix[x1-1][y2] + prefix[x2][y1-1] - prefix[x1-1][y1-1])
    print(answer)
