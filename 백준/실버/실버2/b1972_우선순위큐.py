# 최소 힙
# 백준/1972번

import heapq
import sys
input = sys.stdin.readline

N = int(input()) # 연산의 개수

heap = []
for _ in range(N):
    x = int(input()) # 자연수 x 입력 받기
    if x == 0  : # x가 1이고
        if heap : # 힙 배열이 비어있지 않다면
            print(heapq.heappop(heap)) # 배열에서 가장 작은 값을 출력하고 제거
        else: # 힙 배열이 비어있다면
            print(0) # 0 출력
    else: # x가 0이 아니라면
        heapq.heappush(heap,x) # 힙 배열에 x 추가하기

