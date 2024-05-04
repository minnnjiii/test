# 시험 감독
# 백준/13458번

# 문제
# 필요한 감독관 수의 최소값은? 

import math

n = int(input()) # n개의 시험장
a = list(map(int,input().split()))  # 시험장에 있는 응시자 수 a

# 총감독관이 감시 가능한 응시자 수 b
# 부감독관이 감시 가능한 응시자 수 c
b,c = map(int,input().split()) 

supervisor = 0 # 감독관 수 

for i in a: 
    supervisor += 1  # 총감독관
    if b < i :
        supervisor += math.ceil((i-b) / c) # 부감독관 

print(supervisor)