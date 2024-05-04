# 수 정렬하기
# 2750

n = int(input())

nums = []
for _ in range(n) : 
    nums.append(int(input())) 

nums.sort() 

for num in nums: 
    print(num)