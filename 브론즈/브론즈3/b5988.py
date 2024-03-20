# 홀수일까 짝수일까
# 5988

n = int(input()) 

for _ in range(n) : 
    k = int(input()) 

    if k % 2 == 0 : 
        print("even") 
    else:
        print("odd")