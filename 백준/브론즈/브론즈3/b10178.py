# 할로윈의 사탕

t = int(input()) 

for i in range(t) : 
    c, v = map(int,input().split()) 
    
    print("You get {} piece(s) and your dad gets {} piece(s).".format(c//v,c%v))