# 부호

import sys

input = sys.stdin.readline

for i in range(3) :
    S = 0
    for j in range(int(input())) :
        S += int(input())

        
    if S == 0 :
        print(0)
    elif S > 0 :
        print("+")
    else:
        print("-")