# 달팽이는 올라가고 싶다
# 백준/2869번 

import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())    

if (v-b) % (a-b) == 0 : 
    print((v-b)//(a-b)) 
else:
    print((v-b)//(a-b)+1)