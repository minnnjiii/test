# 2의 제곱인가?
# 백준_11966번 

n = int(input()) 

two = [] 

for i in range(31) : 
    two.append(2**i) 

if n in two : 
    print(1)
else:
    print(0)