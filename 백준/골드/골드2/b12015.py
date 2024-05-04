# 가장 긴 증가하는 부분 수열 2
# 백준/12015번d

import sys
input = sys.stdin.readline


N = int(input()) # 수열의 크기
arr = list(map(int,input().split())) # 수열 A를 이루는 Ai
lis = [0]

for i in arr:
    if lis[-1] < i :
        lis.append(i) 
    else:
        left = 0 
        right = len(lis) 
    
        while left < right : 
            mid = (right + left) // 2 
            if lis[mid] < i : 
                left = mid + 1 
            else : 
                right = mid
        lis[right] = i 

print(len(lis)-1)