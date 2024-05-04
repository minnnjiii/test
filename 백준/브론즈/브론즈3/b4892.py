# 숫자 맞추기 게임 
# 백준/4892번

count = 1 # 케이스 번호
while True:
    n = int(input()) 
    if n == 0 :
        break
    n1 = 3 * n 
    if n1 % 2 == 0 : 
        n2 = n1/2 
    else :
        n2 = (n1+1) /2
    n3 = 3 * n2
    n4 = n3 / 9 
    if n1 % 2 == 0 : 
        print("{}.".format(count),"even",int(n4))
    else:
        print("{}.".format(count),"odd",int(n4))
    count += 1 
