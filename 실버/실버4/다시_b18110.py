# solved.ac
# 백준/18110번

import sys
input = sys.stdin.readline

def _round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)
    
n = int(input())

if n:
    num = []
    for _ in range(n):
        num.append(int(input()))
    
    num.sort()

    ro = _round(n*0.15)
    if ro > 0 :
        print(_round(sum(num[ro:-ro])/len(num[ro:-ro])))
    else:
        print(_round(sum(num)/len(num)))
else:
    print(0)