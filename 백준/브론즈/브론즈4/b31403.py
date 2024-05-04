#  A + B - C

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

print(a+b-c) 

a = str(a)
b = str(b) 

ab = a+b 

print(int(ab)-c)