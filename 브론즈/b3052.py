# 나머지 

nums= []

for i in range(10):
    num = int(input())%42
    if num not in nums:
        nums.append(num)

    
print(len(nums))