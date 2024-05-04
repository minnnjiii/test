# 퇴사
# 백준/14501번

# 으아아아아아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import sys
input = sys.stdin.readline

N = int(input())
table = [[] for _ in range(N+1)]
for i in range(N):
    a, b = map(int, input().split())
    table[i+1] = [a, b]

dp = [-1 for _ in range(N+1)]

def recur(idx):
    global ans

    if idx == N +1 :
        return 0
    
    if idx > N +1 : 
        return -999999999999
    
    if dp[idx] != -1 : # 이미 저장되었다면 
        # 다시 비교하러 들어갈 필요가 없으므로 
        return dp[idx] 
    
    # 상담을 받거나, 안받거나, 그 중에서 더 많은 돈을 버는 경우를 DP테이블에 저장
    dp[idx] = max(recur(idx+table[idx][0] + table[idx][1]), recur(idx+1))

    return dp[idx]


ans = recur(1)
print(ans)