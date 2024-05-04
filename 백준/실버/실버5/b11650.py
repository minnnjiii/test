# 좌표 정렬하기
# 백준/11650번 

import sys
input = sys.stdin.readline

number = []
n = int(input()) 

for _ in range(n):
    number.append(list(map(int,input().split()))) 

number.sort()

for i in range(n):
    print(number[i][0],number[i][1])

