# 벌집
# 백준/2292번

n = int(input()) 
count = 1 
num = 1 

while n > num : 
    num += 6 * count 
    count += 1 
print(count)

  

'''

1~1(0) 1 

2~7 (+6)2

8~19 (+12)3
20~37 (+18) 4 
38~61 (+24) 5
62~91 (+30) 6

'''