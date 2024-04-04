# 연속합
# 백준/1912번

import sys
input = sys.stdin.readline

n = int(input())
prefix = list(map(int,input().split())) 

for i in range(1,n):
    prefix[i] = max(prefix[i]+ prefix[i-1],prefix[i])

print(max(prefix))