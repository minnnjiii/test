# 백준/10815번
# 숫자 카드

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())))

M = int(input()) 
arr2 = list(map(int,input().split()))


for i in range(M):
    left = 0
    right = N - 1 
    
    while left <= right :
        mid = (left + right) // 2

        if arr[mid] == arr2[i] : 
            print(1,end=" ")
            break
        elif arr[mid] < arr2[i] : 
            left = mid + 1 
        else:
            right = mid - 1        
    else:
        print(0,end=" ")

