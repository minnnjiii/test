# 꼬리를 무는 숫자 나열

import sys
input = sys.stdin.readline

num1, num2 = map(int,input().split()) 


'''

좌표 
11 = (3,3) 
33 = (9,1) 

직각거리
(9-3,3-1) = (6,2) = 6+2 =  8


'''



if num1 % 4 == 0 : 
    numX = num1//4
    numY = 4
else : 
    numX = num1//4 +1 # num1의 x좌표
    numY = num1 % 4  # num1의 y좌표

if num2 % 4 == 0 : 
    num2X = num2//4
    num2Y = 4
else : 
    num2X = num2//4 +1 # num2의 x좌표
    num2Y = num2 % 4  # num2의 y좌표


# 직각거리 구하기
print(abs(numX-num2X)+abs(numY-num2Y))
