# 3431. 준환이의 운동관리

T = int(input()) 

for i in range(T):
    L, U , X = map(int,input().split()) 

    if X > U : 
        print("#{}".format(i+1),-1)
    elif X < L : 
        print("#{}".format(i+1),L-X)
    else:
        print("#{}".format(i+1),0)