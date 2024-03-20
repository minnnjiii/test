# 배수 찾기
# 4504

n = int(input()) 

while True:
    num = int(input()) 

    if num == 0 :
        break

    if num % n == 0 :
        print("{} is a multiple of {}.".format(num,n))
    else:
        print("{} is NOT a multiple of {}.".format(num,n))