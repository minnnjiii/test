# 팩토리얼 0의 개수
# 1676번 

import math
import sys
input = sys.stdin.readline

N = int(input())
n = str(math.factorial(N))
count = 0
for i in range(len(n)-1,0,-1):
    if n[i] != '0' : 
        break 
    elif n[i] == '0' : 
        count += 1 

print(count)
