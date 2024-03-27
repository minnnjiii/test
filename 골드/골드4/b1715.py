# 카드 정렬하기
# 백준_1715번
# gold 4 

import sys
import heapq

input = sys.stdin.readline

card = []
for _ in range(int(input())): 
    heapq.heappush(card,int(input()))

total = 0 
while len(card) > 1 :

    # 작은 수 들을 먼저 더해야함
    # 가장 작은 두 수 꺼내기
    a = heapq.heappop(card) 
    b = heapq.heappop(card) 
    
    # 가장 작은 두 수 더하기
    # 합산한 결과를 큐에 넣음 
    total += a + b 
    heapq.heappush(card, a+b)

print(total)

