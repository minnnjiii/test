# 피보나치 수 5
# 백준/10870번

fibo = [0,1]

num = int(input()) 
if num == 0 :
    print(0)
elif num == 1 :
    print(1) 
else:
    for i in range(1,num) : 
        fibo.append(fibo[i]+fibo[i-1]) 


    print(fibo[-1])