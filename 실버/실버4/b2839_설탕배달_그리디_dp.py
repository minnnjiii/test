# 설탕 배달
# 백준_2839번

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 
# 그 수를 구하는 프로그램을 작성하시오.
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

bag = 0

num = int(input()) 

while num >= 0 : 
    if num % 5 == 0 : 
        bag += (num // 5) 
        print(bag) 
        break
    num -= 3
    bag += 1 
else: 
    print(-1)

    