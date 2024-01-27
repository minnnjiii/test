n = int(input())
s = list(map(int,input().split()))
count = 0

for j in s:
    error = 0
    if j > 1:
        for i in range(2,j):
            if j %i == 0 :
                error += 1
        if error == 0:
            count += 1 
print(count)