# 약수 구하기
# 백준_2501번 

n, k = map(int,input().split()) 

num = [] 

for i in range(1,n+1):
    if n % i == 0 : 
        num.append(i)


num.sort()

if k > len(num) : 
    print(0)
else: 
    print(num[k-1])

