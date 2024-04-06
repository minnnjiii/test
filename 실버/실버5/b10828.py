# 백준/10828번
# 스택
# 실버4 

import sys
input = sys.stdin.readline

n = int(input()) 

stack = []
for _ in range(n):
    order= list(map(str,input().split()))
    if order[0] == "push" : 
        stack.append(int(order[1]))
    if order[0] == "top" : 
        if stack: 
            top = stack[-1]
            print(top)
        else:
            print(-1)
    if order[0] == "size":
        print(len(stack))
    if order[0] == "empty":
        if len(stack) > 0 : 
            print(0) 
        else:
            print(1) 
    if order[0] == "pop":
        if len(stack) > 0 :
            print(stack.pop())
        else: 
            print(-1)


