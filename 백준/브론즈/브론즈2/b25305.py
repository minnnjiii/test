# 커트라인
# 백준/25305번

import sys

input = sys.stdin.readline


n, k = map(int,input().split())
score = list(map(int,input().split())) 

score.sort(reverse=True) 

print(score[k-1])