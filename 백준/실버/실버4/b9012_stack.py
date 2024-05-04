# 괄호
# 백준/9012번

import sys
input = sys.stdin.readline

t = int(input()) 


for _ in range(t):
    stack = []
    
    word = input().strip() 
    for i in word: 
        if i == "(":
            stack.append(i) 
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO") 
                break 
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    