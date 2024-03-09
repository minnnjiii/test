# MBTI
# 25640번 

JinhoMBTI = input() 
n = int(input())

count = 0 # mbti 똑같으면 카운트할 변수
for i in range(n):
    f = input() 
    if f == JinhoMBTI : 
        count += 1 

print(count)