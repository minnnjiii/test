# 나는 요리사다

vic = []
for i in range(5) : 
    vic.append(sum(map(int,input().split())))
    
print(vic.index(max(vic))+1,max(vic))