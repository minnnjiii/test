# 나무 자르기
# 백준/2805번

import sys
input = sys.stdin.readline

# 나무의 수 N
# 상근이가 가져가려고 하는 나무의 길이 M
# 절단기에 설정할 수 있는 높이의 최댓값은?

N, M = map(int,input().split()) 
arr = list(map(int,input().split())) 


'''

7이 되려면
5 0 0 2 가 나와야함 

정답 15(높이)인 것을 어떻게 구하지 

시작점과 끝점을 정해 
그리고 그걸로 이분탐색을 하는거지 

근데 그 시작점이 뭐고 끝이 뭔지 



'''

left = 0
right = max(arr) - 1

while left <= right : 
    mid = (left + right) // 2 

    res = 0
    for i in range(N):
        x = arr[i] - mid 
        if x > 0 :
            res += x 
    
    if res == M :
        print(mid) 
        break
    elif res > M : 
        left = mid + 1
    else:
        right = mid - 1


