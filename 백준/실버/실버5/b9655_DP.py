# 백준/9655번
# 돌 게임

import sys
input = sys.stdin.readline

N = int(input()) # 돌의 개수

# DP 테이블 만들어주기(입력값의 최대는 1000)
dp = [-1] * 1001

dp[1] = 1 #상근
dp[2] = 0 #창영
dp[3] = 1 #상근

for i in range(4, N+1): 
    if dp[i-1] != 1 or dp[i-3] != 1:
        dp[i] = 1 
    else:
        dp[i] = 0


if dp[N] == 1:
    print("SK")
else:
    print("CY")




# 단순 구현 풀이 (DP 풀이 ❎)
# N = int(input()) # 돌 N개

# if N % 2 == 0 :
#     print("CY")
# else: 
#     print("SK")