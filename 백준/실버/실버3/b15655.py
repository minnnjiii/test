# 백준/15655번
# N과 M(6)

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
Ni = list(map(int,input().split()))
Ni.sort(reverse=False) 

arr = []

def recur(num):

    if len(arr) == M :
        print(*arr)
        return
    
    for i in range(num,N):
        if Ni[i] in arr:
            continue

        arr.append(Ni[i])
        recur(i+1)
        arr.pop()

recur(0)