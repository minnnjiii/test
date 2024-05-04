# 암호제작
# 백준_1837번

# 두 소수 p와 q의 곱으로 이루어진 암호 P가 좋은 암호인지 좋지 않은 암호인지 구하시오
# 암호가 좋은 암호이면 "GOOD" 출력
# 좋지 않은 암호이면 "BAD"와 소수 r (두 소수 중 작은 소수) 출력

# 암호 P와 K
P, K = map(int,input().split()) 



for i in range(2,K) : 
        if P % i == 0 : 
            print("BAD",i)
            break
else:
      print("GOOD")

