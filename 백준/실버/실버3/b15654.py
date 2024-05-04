# 백준/15654번
# N과 M(5)

import sys
input = sys.stdin.readline

# N개의 자연 수 중에서 M개를 고른 수열
# N개의 자연수 
N, M = map(int,input().split())
Ni = list(map(int,input().split()))
Ni.sort(reverse=False)
arr = []

def recur():

    if len(arr) == M :
        print(*arr)
        return
    
    for i in Ni:
        if i in arr:
            continue
        arr.append(i)
        recur()
        arr.pop()

recur()