# 특식 배부
# 27110번

n = int(input()) # 주문한 각 종류의 치킨 마릿수 n 
a, b, c = map(int,input().split()) # 각각의 치킨을 선호하는 병사의 수

sum = 0 

if a > n : 
    sum += n 
else : 
    sum += a

if b > n : 
    sum += n 
else : 
    sum += b

if c > n : 
    sum += n
else : 
    sum += c

print(sum)