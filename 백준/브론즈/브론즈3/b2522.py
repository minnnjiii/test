# 별 찍기 - 12

n = int(input())

for j in range(n-1,0,-1):
    print(j*(" ")+(n-j)*("*"))
for i in range(0,n):
    print(i*" "+"*"*(n-i))
