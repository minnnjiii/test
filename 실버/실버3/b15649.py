# 백준/15649번
# N과 M(1)

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = []
def recur(number):
    for i in range(1,N+1):
        if i in arr:
            continue
        arr.append(i)
        recur(number+1)
        arr.pop()

    if number == M:
        print(*arr)
        return 

    

recur(0)

