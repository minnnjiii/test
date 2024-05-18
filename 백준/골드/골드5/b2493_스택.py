# 백준/2493번
# 탑
# 각각의 탑에서 발사한 레이저 신호를 
# 어느 탑에서 수신하는지 

import sys
input = sys.stdin.readline

N = int(input()) # 탑의 수 
arr = [0] + list(map(int,input().split())) # 탑의 높이 배열
res = [0] * (N + 1) 

stack = [] # [(탑의 인덱스, 탑의 높이)]

for i in range(1, N + 1) : 

    while stack:

        # 현재 높이가 stack의 높이보다 크다면
        if arr[i] > stack[-1][0] :
            stack.pop() # stack 지우기
        # 그게 아니라면
        else:
            res[i] = stack[-1][1]  # 현재 위치의 레이저를 수신받을 수 있는 탑의 위치 저장
            break

    stack.append((arr[i], i))

for i in range(1, N + 1) :
    print(res[i], end = " ")


