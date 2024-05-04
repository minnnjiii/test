# 보석 도둑_b14232

n = int(input())
jewel = [] 

for i in range(1,int(n**0.5)+1):
    if i >2 :
        if n%i == 0:
            jewel.append(i)
            jewel.append(n//i)

jewel.sort()
print(len(jewel))
print(' '.join(map(str,jewel)))