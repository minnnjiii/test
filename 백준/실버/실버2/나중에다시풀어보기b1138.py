# 한 줄로 서기
# 백준/1138번

import sys
input = sys.stdin.readline

N = int(input()) # 사람의 수
arr = list(map(int,input().split())) 

ans = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i] and ans[j] == 0 :
            ans[j] = i + 1
            break
        elif ans[j] == 0 :
            cnt += 1 

print(' '.join(map(str, ans)))