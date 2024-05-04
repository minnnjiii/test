# 2×n 타일링
# 백준/11726번

import sys
input = sys.stdin.readline

sys.setrecursionlimit(9999)
N = int(input())

ans = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0 :
        ans[0] = 1 
    elif i == 1 :
        ans[1] = 1
    else:
        ans[i] = ans[i-1]+ans[i-2] 
        
print(ans[-1]%10007)