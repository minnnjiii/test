# 백준/15651번
# N과 M(3)


import sys
input = sys.stdin.readline


N,M = map(int,input().split())

arr = []
def recur(number):

    if number == M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        arr.append(i)
        recur(number+1)
        arr.pop()

recur(0)