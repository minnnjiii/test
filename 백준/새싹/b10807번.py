# 개수 세기

# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

N = int(input())
num = list(map(int,input().split()))
v = int(input())

print(num.count(v))