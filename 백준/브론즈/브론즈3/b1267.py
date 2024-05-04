# 핸드폰 요금

import sys
input = sys.stdin.readline


'''


영식 요금제 30초마다 10원씩, 0~29초 = 10원, 30~59초 = 20원
민식 요금제 60초마다 15원씩, 0~59초 = 15원, 60초~119초 = 30원


'''


n = int(input()) # 저번 달에 이용한 통화의 개수

call = list(map(int,input().split())) # 통화 시간 n개 

Y = 0 
M = 0 
for i in range(len(call)):
    Y += (call[i-1] // 30 ) + 1
    M += (call[i-1] // 60) +1 

Y *= 10 # 10초 
M *= 15 # 15초

if Y < M : 
    print("Y", Y)
elif Y > M : 
    print("M", M)
else : 
    print("Y", "M", Y)