# 소수 구하기
# 백준/1929번

import sys
input = sys.stdin.readline

m,n = map(int,input().split())

for i in range(m,n+1):

    if i == 0 :
        continue
    if i == 1:
        continue

    for j in range(2,int(i**0.5)+1): 
        if i % j == 0 : 
            break
        
    else: 
        print(i)