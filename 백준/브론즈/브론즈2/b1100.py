# 하얀 칸

import sys
input = sys.stdin.readline

count = 0 

for _ in range(4):
    chess = list(map(str,input().strip()))
    chess2 = list(map(str,input().strip()))
    for i in range(0,8,2):
        if chess[i] == 'F':
            count += 1 
    for j in range(1,8,2):
        if chess2[j] == 'F':
            count += 1

print(count)