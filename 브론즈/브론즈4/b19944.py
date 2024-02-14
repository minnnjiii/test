#뉴비의 기준은 뭘까?_19944

N, M = map(int,input().split())

if M <= 2:
    print("NEWBIE!")
elif M > 2 and M <= N:
    print("OLDBIE!")
else:
    
    print("TLE!")