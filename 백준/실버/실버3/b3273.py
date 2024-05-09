# 두 수의 합
# 백준/3273번

import sys
input = sys.stdin.readline


n = int(input()) 
arr = list(map(int,input().split())) 
ans = int(input())

arr.sort()
cnt = 0
while True:
    for i in range(n):
        if arr[i] + arr[-1] == ans:
            cnt += 1 
            