# 수열
# 백준/2559번 

import sys
input = sys.stdin.readline

n, k = map(int,input().split()) 

answer = [] 

nSet = list(map(int,input().split())) 

answer.append(sum(nSet[0:k]))

for i in range(0,n-k):
    answer.append(answer[i]-nSet[i]+nSet[i+k]) 

print(max(answer))