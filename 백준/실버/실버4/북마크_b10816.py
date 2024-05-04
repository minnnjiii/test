# 숫자 카드 2
# 백준/10816번

import sys

input = sys.stdin.readline

N = int(input()) 
number = list(map(int,input().split()))
M = int(input())
numberM = list(map(int,input().split()))

ans = {}

for n in number:
    if n in ans:
        ans[n] += 1
        
    else:
        ans[n] = 1
        
for m in numberM:
    if m in ans:
        print(ans[m], end=' ')
    else:
        print(0,end = ' ')
    