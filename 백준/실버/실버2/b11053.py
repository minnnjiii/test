

# 가장 긴 증가하는 부분 수열
# 백준/11053번

import sys
input = sys.stdin.readline


N = int(input()) # 수열의 크기
arr = list(map(int,input().split())) # 수열 A를 이루는 Ai

# dp테이블 만들어주기
dp = [1 for _ in range(N)]  

for i in range(N): 
    for j in range(i): # 현재 위치보다 왼쪽에 있는 값들만 비교
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1) 


print(max(dp))