# 막대기
# 백준/17608번

import sys
input = sys.stdin.readline

N = int(input()) # 막대기 갯수
stack = []
for _ in range(N):
    stack.append(int(input())) 

last = stack[-1]
cnt = 1
for i in reversed(range(N)):
    if stack[i] > last :
        cnt += 1
        last = stack[i]
    
print(cnt)