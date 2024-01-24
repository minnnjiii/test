# 시험 점수

S = list(map(int,input().split()))
T = list(map(int,input().split()))

if sum(S) == sum(T) : 
    print(sum(S))
else: 
    print(max(sum(S),sum(T)))
