# 모음의 개수


while True:
    post = input()
    if post == "#" : 
        break
    count = 0 
    
    for i in post:
        if i in 'AEIOUaeiou':
            count += 1 
    print(count)