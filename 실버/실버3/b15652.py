# 백준/15652번
# N과 M(4)

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨
# 고른 수열은 비내림차순이어야 함

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []


def recur(number):

    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(number,N+1):
        arr.append(i)
        recur(i)
        arr.pop()

recur(1)