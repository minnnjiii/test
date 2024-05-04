# Hashing
# 백준/15829번

import sys
input = sys.stdin.readline

L = int(input())
word = input().strip()

res = 0
count = 0
for i in word:
    res += (ord(i)-96) * 31**(count)
    count += 1
print(res % 1234567891)