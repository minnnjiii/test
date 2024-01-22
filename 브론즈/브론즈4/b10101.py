# 삼각형 외우기

t1 = int(input())
t2 = int(input())
t3 = int(input())

if t1 == t2 == t3 == 60 :
    print("Equilateral")
elif t1 + t2 + t3 == 180 :
    if t1 == t2 or t2 == t3 or t3 == t1 : 
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")