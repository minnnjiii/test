# 세 막대

triangle = list(map(int,input().split()) )

triangle.sort()

while True:

    if triangle[0]+triangle[1] > triangle[2] :
        break 

    triangle[2] -= 1 

print(sum(triangle))