# 등장하지 않는 문자의 합
# 백준/3059

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input()) # 테스트 데이터 갯수

for _ in range(t) : 
    asc = [] 
    s = input()
    for i in alphabet : 
        if i not in s : 
            asc.append(ord(i))
    print(sum(asc))