# 최대공약수와 최소공배수
# 백준/2609번

import sys
input = sys.stdin.readline

def _gcd(a,b):
    if b == 0 :
        return a 
    return _gcd(b,a%b)

m,n = map(int,input().split()) 

print(_gcd(m,n)) 
print((m*n)//_gcd(m,n))