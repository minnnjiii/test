# 창고 다각형
# 백준/2304번

# 알고리즘 분류
# 완탐, 누적합, 투포인터, 스택

import sys
input = sys.stdin.readline


pillar = [] # 기둥

N = int(input()) # 기둥의 개수
for _ in range(N):
    # 위치를 나타내는 정수 L(x축), 높이를 나타내는 정수 H(y축)를 리스트로 입력받기
    pillar.append(list(map(int,input().split())))

pillar.sort() # 위치(x축)를 기준으로 정렬 


# sorted를 사용하여 y축 기준으로 정렬한 리스트를 변수 maxpillar에 담음
maxpillar = sorted(pillar,key=lambda x:x[1]) 

# 기둥들 중 제일 높은 기둥의 index를 highH라는 변수에 담음
highH = pillar.index(maxpillar[-1])

# 이제부터 res라는 변수에 계산한 면적을 담기 
# 우선 가장 높은 기둥의 면적을 res에 담음
res = pillar[highH][1] 


# 초기 높이 = 제일 왼쪽 기둥
high = pillar[0][1]
for i in range(highH):
    if high < pillar[i+1][1] : # 기존의 제일 높은 기둥보다 높다면
        res += high * (pillar[i+1][0]-pillar[i][0]) # 현재 면적 계산
        high = pillar[i+1][1] # 다음 기둥으로 갱신
    else:
        res += high * (pillar[i+1][0]-pillar[i][0])

# 초기 높이 = 제일 오른쪽 기둥
high = pillar[-1][1]
for j in range(N-1,highH,-1):
    if high < pillar[j-1][1]:
        res += high * (pillar[j][0]-pillar[j-1][0])
        high = pillar[j-1][1]
    else:
        res += high * (pillar[j][0]-pillar[j-1][0])

print(res)