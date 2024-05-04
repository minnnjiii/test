# 열 개씩 끊어 출력하기

post = input()

for i in range(0,len(post),10):
    print(post[i:i+10])
    
