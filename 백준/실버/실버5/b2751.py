# 수 정렬하기 2
# 백준/2751번 

import sys
input = sys.stdin.readline

n = int(input()) 

ans=[]

for _ in range(n):
    ans.append(int(input())) 

ans.sort() 

for i in ans:
    print(i)
