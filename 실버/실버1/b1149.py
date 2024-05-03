# RGB거리
# 백준/1149번

import sys
input = sys.stdin.readline

N = int(input()) 

house = [list(map(int,input().split())) for _ in range(N)] 

prefix = [ [0] * 3 for _ in range(N)]

prefix[0] = house[0]

for i in range(1,N):
    prefix[i][0] = house[i][0] + min(prefix[i-1][1], prefix[i-1][2])
    prefix[i][1] = house[i][1] + min(prefix[i-1][0], prefix[i-1][2])
    prefix[i][2] = house[i][2] + min(prefix[i-1][0], prefix[i-1][1])

print(min(prefix[-1]))