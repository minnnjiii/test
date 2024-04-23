# 이항 계수 1
# 백준/11050번

import math
import sys
input = sys.stdin.readline

def bino_factorial(n,k):
    return math.factorial(n) // (math.factorial(n-k)*math.factorial(k))

N,K = map(int,input().split())
print(bino_factorial(N,K))