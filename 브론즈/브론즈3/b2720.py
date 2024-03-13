# 세탁소 사장 동혁

t = int(input())

for i in range(t):
    cent = int(input())
    a = cent // 25 
    if a > 0 : 
        cent = cent - 25*a 
    b = cent // 10 
    if b > 0 : 
        cent = cent - 10*b
    c = cent // 5
    if c>0 : 
        cent = cent - 5*c
    d = cent // 1 
    if d>0:
        cent = cent - 1*d 
    print(a,b,c,d)