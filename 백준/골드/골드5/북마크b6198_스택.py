# 옥상 정원 꾸미기
# 백준/6198번

import sys
input = sys.stdin.readline

N = int(input()) 

building = [0]
res = [0] * (N + 1) 

stack = []

for _ in range(N):
    building.append(int(input())) 

for i in range(1,N+1) :
    
    while stack :
        
        if building[i] < stack[-1] : 
            stack.pop() 
        else:
            res[i] = stack[-1]
            break

    stack.append(i) #  빌딩 높이


print(res)