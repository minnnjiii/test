# LCS
# 백준/9251번
# Longest Common Subsequence, 최장 공통 부분 수열

import sys
input = sys.stdin.readline

# 수열 a, b 입력받기
a = list(str(input().strip()))
b = list(str(input().strip()))

# dp테이블 만들기
dp = [[0 for _ in range(len(b)+1)]for _ in range(len(a)+1)]


for i in range(1,len(a) +1): # 수열 a에서 하나씩 가져오기
	for j in range(1,len(b) +1): # 수열 b에서 하나씩 가져오기
		if a[i-1] == b[j-1]: # 비교하려는 문자가 똑같다면
			dp[i][j] = dp[i-1][j-1]+ 1 # 대각선 위의 값에서 +1
		else: # 그게 아니라면 왼쪽과 위에서 큰 값을 그대로 가져옴
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	
print(dp[len(a)][len(b)])
