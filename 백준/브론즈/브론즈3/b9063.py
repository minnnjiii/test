# 대지

import sys
input = sys.stdin.readline

n = int(input()) 

xs = [] # x좌표
ys = []  # y좌표
for i in range(n) : 
    x, y = map(int,input().split()) 
    xs.append(x)
    ys.append(y) 

print((max(xs)-min(xs))*(max(ys)-min(ys)))