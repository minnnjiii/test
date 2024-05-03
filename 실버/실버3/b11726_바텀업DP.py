# 2×n 타일링
# 백준/11726번

import sys
input = sys.stdin.readline



N = int(input())

ans = [0 for i in range(N+1)]
ans[1] = 1
ans[2] = 2

for i in range(3,N+1):
    ans[i] = ans[i-1]+ans[i-2] 

print(ans[N]%10007)