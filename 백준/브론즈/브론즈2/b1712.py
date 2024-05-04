# 손익분기점
# 백준/1712번

import sys
input = sys.stdin.readline
a, b, c = map(int,input().split()) 

if b >= c : 
    print(-1) 
else:
    print(int(a/(c-b)+1))