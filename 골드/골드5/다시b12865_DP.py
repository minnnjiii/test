# 평범한 배낭
# 백준/12865번 

# 탑다운
import sys
input = sys.stdin.readline

sys.setrecursionlimit(999999)

def recur(idx, kilo ):
    global ans

    if kilo > K : return -9999999

    if idx == N : 
        return 0 
    
    if dp[idx][kilo] != -1:
        return dp[idx][kilo]
    
    dp[idx][kilo] = max(recur(idx+1, kilo + bag[idx][0]) + bag[idx][1], recur(idx+1,kilo))

    return dp[idx][kilo]

N, K = map(int,input().split())


ans = 0

bag = [list(map(int,input().split())) for i in range(N)]
# 물건 갯수만큼 dp테이블을 만들어주기
dp = [[-1 for _ in range(100010)] for _ in range(N)] # 2차원 dp

ans = recur(0,0)
print(ans)
