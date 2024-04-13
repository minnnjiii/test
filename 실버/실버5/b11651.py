# 좌표 정렬하기 2
# 백준/11651번

import sys

input = sys.stdin.readline

N = int(input())

num = []
for _ in range(N):
    num.append(list(map(int,input().split())))

num.sort(key=lambda x : (x[1],x[0]))

for i in num:
    print(*i)