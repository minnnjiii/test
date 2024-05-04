# 모음의 개수_b10987

word = input()
mo = ['a','e','i','o','u']

cnt = 0
for i in mo:
    cnt += word.count(i)
    
print(cnt)