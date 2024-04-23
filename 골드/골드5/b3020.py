# 개똥벌레
# 백준/3020번
# 골드5

from collections import Counter
import sys
input = sys.stdin.readline

# 동굴 길이 N, 동굴 높이 H
N, H = map(int,input().split())

# 장애물의 크기 입력받기
obstacle = [] 
for _ in range(N):
    obstacle.append(int(input()))

# 핵심 부분⬇️
prefix = [0 for _ in range(H+1)]
for i in range(N):
    # 석순일 때 
    if i % 2 == 0:
        prefix[0] += 1
        prefix[obstacle[i]] -= 1
        
    # 종유석일 때
    else:
        prefix[-(obstacle[i]+1)] += 1
        prefix[-1] -= 1
     
# 누적합 만들기
ans = [0 for _ in range(H+1)]
for j in range(0,H):
    ans[j+1] = ans[j] + prefix[j] 

# 누적합 만들 때 생성된 0 제거 
del(ans[0])

# 장애물의 최솟값을 구해야 하니까
# 누적합 리스트에서 "최소값" 구하기 
# Counter 모듈을 사용하여 구간의 수 구하기
print(min(ans),  Counter(ans)[min(ans)]  )