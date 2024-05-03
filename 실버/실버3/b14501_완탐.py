# 퇴사
# 백준/14501번

import sys
input = sys.stdin.readline

N = int(input())

consult = []
for _ in range(N):
    consult.append(list(map(int,input().split()))) 


def recur(idx,money):
    global ans

    if idx == N  :
        
        ans = max(ans,money)
        return
    if idx > N : 
        return
    
    
    recur(idx+consult[idx][0],money+consult[idx][1])
    recur(idx+1,money)

ans = 0
recur(0,0)

print(ans)