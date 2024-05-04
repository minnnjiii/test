# 1945. 간단한 소인수분해 

T = int(input())

num = []
for _ in range(T):
    num.append(int(input())) 

for i in range(T): 
    j = 2 
    number = num[i] 
    ans = []
    while number > 1:
        if number % j == 0 : 
            number /= j 
            ans.append(j)
        else:
            j += 1 

    answer = []
    for k in [2,3,5,7,11]: 
        sosu = ans.count(k)
        if sosu:
            answer.append(sosu)
        else:
            answer.append(0)
    print("#{}".format(i+1),*answer)