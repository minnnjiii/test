# 프린터 큐
# 백준/1966번 


import sys
input = sys.stdin.readline

t = int(input()) 
for _ in range(t):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))
    
    count = 1 
    while num:
        if num[0] < max(num):
            num.append(num.pop(0))
        else:
            if M == 0:
                break
            num.pop(0)
            count += 1


        M = M - 1 if M > 0 else len(num) -1 # python 조건부 표현식
    
    print(count)