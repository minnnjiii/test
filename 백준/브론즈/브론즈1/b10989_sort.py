# 수 정렬하기 3
# 백준/10989번

import sys
input = sys.stdin.readline

arr = [0] * 10001

for _ in range(int(input())):
    num = int(input()) 
    arr[num] += 1 

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)