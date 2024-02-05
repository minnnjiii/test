#최댓값_2566
num = []
for i in range(9): 
    num += list(map(int,input().split()))

number = (num.index(max(num)) // 9) +1 
numbers = num.index(max(num)) - (9*(number-1))
print(max(num))
print(number,numbers+1)


