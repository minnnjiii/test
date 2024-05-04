# 평균 _ 1546번 

N = int(input())
score = list(map(int,input().split()))

sum = 0
for i in score:
    sum += i/max(score)*100

print(sum / len(score))