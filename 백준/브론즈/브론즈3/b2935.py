# 소음

import sys
input = sys.stdin.readline

A = int(input()) 
cal = input().strip()
B = int(input()) 

if cal == "+" : 
    print(A+B)
elif cal == "*":
    print(A*B)