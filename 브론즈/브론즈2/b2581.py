# 소수
# 백준/2581번

m = int(input()) 
n = int(input()) 

num = []



for i in range(m,n+1) : 
    error = 0
    if i > 1 :
        for j in range(2,i) : 
            if i % j == 0 : 
                error += 1
                break
        if error == 0 :
            num.append(i) 

if not num : 
    print(-1) 
else:
    print(sum(num))
    print(min(num))    