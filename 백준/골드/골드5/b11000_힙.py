# 강의실 배정
# b11000.py


import sys
import heapq
input = sys.stdin.readline

lecture = []
n = int(input())  # 강의실 개수 
for _ in range(n) : 
    s,t = map(int,input().split()) 
    lecture.append((s,t))

lecture.sort(key=lambda x : (x[0],x[1]))

# 초기 힙 상태 설정
heap = [lecture[0][1]] # lecture의 리스트의 첫번째 요소의 두번째 값, 즉 첫번째 강의의 종료 시간이 저장됨

for i in range(1,n) : # n은 강의실 개수였음
    # 힙의 가장 작은 요소(루트 노드)와 현재 강의(lecture[i])의 시작 시간을 비교하였을 때
    if heap[0] <= lecture[i][0] : # 해당 종료 시간이 i 시간의 시작 시간 보다 작거나 같다면
        heapq.heappop(heap) # 가장 작은 값(루트 노드) 삭제되고 반환
    heapq.heappush(heap,lecture[i][1]) # 현재 i 시간의 종료 시간을 힙에 추가함

print(len(heap))









# 💡 알고리즘 분류
# 자료구조 
# 그리디 알고리즘
# 정렬
# 우선순위 큐






'''

# 틀린 코드 (근데 왜 틀렸는지 모르겠음 ㅜ... )
# 알고리즘 분류에 그리디 말고 우선순위 큐가 있던데 우선순위 큐 공부해야겠다. 

n = int(input()) 

lecture = [] 
for _ in range(n): 
    s, t = map(int,input().split()) 

    lecture.append((s,t)) 

lecture.sort(key=lambda x : (x[1],x[0]))

last_lecture = 0 # 마지막 강의실 사용종료 시간
count = 0 # 강의실 개수
for s, t in lecture : 
    if s >= last_lecture : 
        count += 1
        last_lecture = t

print(count)

'''
