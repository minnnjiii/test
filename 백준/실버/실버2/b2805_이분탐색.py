# 나무 자르기
# 백준/2805번

import sys
input = sys.stdin.readline

# 나무의 수 N
# 상근이가 가져가려고 하는 나무의 길이 M
# 절단기에 설정할 수 있는 높이의 최댓값은?

N, M = map(int,input().split()) 
arr = list(map(int,input().split())) 




left = 0
right = max(arr)

while left <= right: 
    mid = (left + right) // 2 

    res = 0
    for i in arr:
        if i >= mid :
            res += i - mid

    if res >= M : 
        left = mid + 1
    else:
        right = mid - 1

print(right)