# 두 수의 합
# 백준/3273번

import sys
input = sys.stdin.readline


n = int(input()) 
arr = sorted(list(map(int,input().split())))
x = int(input())


# 두 개의 마우스 커서, 포인터

s = 0
e = n-1


cnt = 0
while s < e: # s == e 만나면 멈추기

    # 정답 조건
    if arr[s] + arr[e] == x:
        cnt += 1 

    if arr[s] + arr[e] >= x : 
        e -= 1 
    else:
        s += 1 



print(cnt)