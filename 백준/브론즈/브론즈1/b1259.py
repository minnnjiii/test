# 팰린드롬수 
# 백준/1259번 

import sys
input = sys.stdin.readline 

while True: 
    num = input().strip() 
    if num == "0" : 
        break
    if num[::-1] == num :
        print("yes") 
    else:
        print("no")
