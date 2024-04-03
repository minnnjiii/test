# 최소공배수
# 백준/1934번

import sys
input = sys.stdin.readline

# 💡 최소 공배수 = (A*B / 최대공약수)

# 최대공약수 구하기 
def gcd(m,n):
    if n == 0 : 
        return m
    return gcd(n,m%n)

num = int(input()) 
for _ in range(num):
    A, B = map(int,input().split())
    print(int(A*B/gcd(A,B)))