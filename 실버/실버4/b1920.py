# 수 찾기
# 백준/1920번

import sys
input = sys.stdin.readline

n = int(input()) 
n_num = set(map(int,input().split())) 

m = int(input()) 
m_num = list(map(int,input().split())) 

for i in range(m):
    if m_num[i] in n_num : 
        print(1)
    else:
        print(0)