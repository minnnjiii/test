# 전깃줄
# 백준/2565번

import sys
input = sys.stdin.readline

T = int(input()) 

arr = [list(map(int,input().split())) for _ in range(T)]

arr.sort() 
print(arr)
dp = [1] * T
for i in range(T):
    for j in range(i):
        if arr[i][1] > arr[j][1] : 
            dp[i] = max(dp[i],dp[j]+1) 

# T - 최대 전깃줄의 수
print(T - max(dp)) 
