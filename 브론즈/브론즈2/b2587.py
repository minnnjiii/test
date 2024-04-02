# 대표값2
# 백준/2587번

num = []

for i in range(5):
    num.append(int(input())) 

num.sort()

print(int((sum(num))/5))
print(num[2])