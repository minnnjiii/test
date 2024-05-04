# 공

import sys
input = sys.stdin.readline

M = int(input()) # 컵의 위치를 바꾼 횟수

ball = [1, 2, 3]
for i in range(M):
    X, Y = map(int,input().split()) 
    
    ball[X-1],ball[Y-1] = ball[Y-1] ,ball[X-1]
    
print(ball.index(1)+1)