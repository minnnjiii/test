# 윷놀이 
# 2490번


for i in range(3):
    count = 0
    y = list(map(int,input().split()))
    for j in y : 
        if j == 1 : 
            count += 1 
    if count == 1 : 
        print("C")
    elif count == 2 : 
        print("B")
    elif count == 3 :
        print("A")
    elif count == 4: 

        print("E")
    elif count == 0 : 
        print("D")