# 12368. 24시간

T = int(input()) 

for i in range(T): 
    A, B = map(int,input().split()) 
    num = A+B 
    print("#{}".format(i+1),num%24)