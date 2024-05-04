# 직각삼각형

while True: 
    listt = list(map(int,input().split()))
    if listt[0] ==  listt[1] == listt[2] == 0: 
        break
    
    listt.sort()
    
    a = listt[0]
    b = listt[1]
    c = listt[2]
    
    a *= a
    b *= b
    c *= c
    
    if a + b == c :
        print("right")
    else:
        print("wrong")