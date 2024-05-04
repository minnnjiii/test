# 삼각형과 세 변
# 5073

while True:
    triangle = list(map(int,input().split()))
    triangle.sort()
    
    if triangle[0] == triangle[1] == triangle[2] == 0 :
        break 
    elif triangle[2] >= ( triangle[0] + triangle[1]) :
        print("Invalid")
    elif triangle[0] == triangle[1] == triangle[2] :
        print("Equilateral")
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2] : 
        print("Isosceles")
    elif triangle[0] != triangle[1] and triangle[1] != triangle[2] and triangle[0] != triangle[2]:
        print("Scalene")
