# 마인크래프트
# 백준/18111번

import sys
input = sys.stdin.readline

# 세로 N, 가로 M, 인벤토리에 들어있는 블록 수 B
N, M, B = map(int,input().split())

ground = []
for _ in range(N):
    ground.extend(map(int,input().split()))

time = [0 for i in range(257)]

h = 0 

# g = 현재 땅 높이
for g in range(257):
    block = B 
    for i in ground:
        if i <= g : 
            time[g] += g - i
            block -= g - i
        else :
            time[g] += 2 * (i - g)
            block += i - g
    
    # ground 집터를 모두 순회한 이후 
    # block의 수가 0 이상이고
    # 현재 땅 높이에서의 소요시간이 짧거나 같으면 
    # h값은 현재 땅 높이로 업데이트 
    if block >= 0 and time[g] <= time[h]:
        h = g 

print(time[h],h)