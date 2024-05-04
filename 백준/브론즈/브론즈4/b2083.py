# 럭비 클럽

while True:
    name, age, kilo = map(str,input().split())
    
    if name == "#" and int(age) == int(kilo) == 0 : 
        break 
    
    if int(age) > 17 or int(kilo) >= 80:
        print(name, "Senior")
        
    else:
        print(name, "Junior")