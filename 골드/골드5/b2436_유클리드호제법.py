# 공약수 
# 백준/2436번

import sys
input = sys.stdin.readline

# 최대공약수 구하기
def _gcd(m,n):
    if n == 0 : 
        return m
    return int(_gcd(n,m%n))

# 최소 공배수
def _lcm(m,n):
    return int(m*n/_gcd(m,n))

# 최대공약수, 최소공배수 입력받기
gcd,lcm = map(int,input().split())


multiple = gcd * lcm 

answer = []
for i in range(gcd,int(multiple**0.5)+1,gcd):
    if _gcd(i, (multiple//i)) == gcd:
        if _lcm(i, (multiple//i)) == lcm:
            answer.append((i,multiple//i))

print(*answer[-1])