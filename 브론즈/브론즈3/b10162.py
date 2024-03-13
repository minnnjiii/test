# 전자레인지

t = int(input()) 

a = t // 300 
if a > 0 : 
    t = t - a*300

b = t//60 
if b > 0:
    t = t-b*60 

c = t // 10
if c > 0 : 
    t = t-c*10 

if t > 0 :
    print(-1)
else:
    print(a,b,c)
