# 2072. 홀수만 더하기

t = int(input())

numi = []
for _ in range(t):
    numi.append(list(map(int,input().split()))) 
    
for i in range(t):
    ans = 0
    for j in numi[i]:
        if j%2 != 0 : 
            ans += j 
    print("#{}".format(i+1),ans) 

