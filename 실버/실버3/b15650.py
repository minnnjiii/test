# 백준/15650번
# N과 M(2)

import sys
input = sys.stdin.readline


def recur(start):

    for i in range(start,N+1):
        if i in arr:
            continue
        arr.append(i)
        recur(i+1)
        arr.pop()

    if len(arr) == M:  
        print(*arr)
        return 
    
N, M = map(int,input().split())
arr = []  
recur(1)

