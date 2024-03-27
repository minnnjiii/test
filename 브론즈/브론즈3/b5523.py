# 경기 결과
# 5523

import sys

input = sys.stdin.readline 

winA = winB = 0
for _ in range(int(input())) : 
    a, b = map(int,input().split()) 
    if a < b : 
        winB += 1
    elif a > b : 
        winA += 1 

print(winA, winB)
