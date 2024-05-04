# 캥거루 세마리
# 2965 

a,b,c = map(int,input().split()) 

if abs(a-b) == 1 and abs(b-c) == 1 : 
    print(0)
else : 
   print(max((abs(a-b)-1),(abs(b-c)-1) ))
