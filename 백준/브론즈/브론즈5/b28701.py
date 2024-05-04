N = int(input())

sum = 0
sum3 = 0
for i in range(1,N+1):
    sum += i
    sum3 += i ** 3
    
print(sum)
print(sum**2)
#print(pow(sum,2))
print(sum3)