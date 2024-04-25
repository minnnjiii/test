# 백준/15656번
# N과 M(7)

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
Ni = list(map(int,input().split()))

Ni.sort()
arr = []

def recur():
    
    if len(arr) == M:
        print(*arr)
        return
    
    for i in Ni:
        arr.append(i)
        recur()
        arr.pop()

recur()