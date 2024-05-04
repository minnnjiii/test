# 도미노
# 2921

# 점이 몇 개 찍혀 있는지 

n = int(input()) 

'''
    
0 = 0 
1 = 3 (+3) 
2 = 12 (+9) 
3 = 30 (+18)
4 = 60 (+30)
5 = 105 (+45) 


'''

ans = 0 
a = 0
b = 0

for i in range(n) : 
    a += 3 
    b += a 
    ans += b 



print(ans)