# 백준/1010번
# 다리 놓기

import sys
input = sys.stdin.readline

# 다리를 지을 수 있는 경우의 수를 계산해주는 함수
def recur(x,y):

    # dp테이블 만들어주기
    dp = [ [1] * (M + 1) for _ in range(N+1)]

    # N이 1일 때 경우의 수는 M과 같음
    for i in range(2,M+1):
        dp[1][i] = i 
        # 예 : dp[1][2] = 2 

    # 점화식 적용(graph[x,y] = grpah[x-1,y] + graph[x-1,y-1])
    for i in range(2, N + 1) : # x좌표부터 채워야함
        for j in range(i+1,M+1) : 
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    return dp[x][y] # 우리가 궁금한건 x,y일 때 경우의 수니까 dp[x][y] 를 return해줌


T = int(input()) # 테스트 케이스의 개수 T
for _ in range(T) : 
    N, M = map(int,input().split()) # 서쪽 사이트 개수 N, 동쪽 사이트 개수 M
    print(recur(N,M)) # 경우의 수 출력

            