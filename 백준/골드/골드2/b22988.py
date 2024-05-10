# 재활용 캠페인
# 백준/22988번

import sys
input = sys.stdin.readline


N, X = map(int,input().split()) 
arr = sorted(list(map(int,input().split())))

s = 0 
e = N - 1

remain = 0
cnt = 0
while s <= e : 
    if arr[e] == X :
        cnt += 1
        e -= 1
        continue

    if s == e :
        remain += 1 
        break
    
    if arr[e] + arr[s] >= X/2 : 
        cnt += 1
        s += 1
        e -= 1
    else:
        s += 1 
        remain += 1 

print(cnt + remain//3)